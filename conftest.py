import pychrome
import pytest

from selenium import webdriver


#------------------Suite setup/Suite teardown fixture---------------------------#
@pytest.fixture(scope='session', autouse=True)
def connection():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    chrome_options.add_argument("--remote-debugging-port=8000")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver # Here tests are executed, driver is delivered to test case
    driver.quit()
    del driver


@pytest.fixture(scope='session')
def connection_with_capturing_network_traffic(connection):

    def output_on_start(**kwargs):
        print(f"START {kwargs}")

    def output_on_end(**kwargs):
        print(f"FINISHED {kwargs}")

    dev_tools = pychrome.Browser(url="http://localhost:8000")
    tab = dev_tools.list_tab()[0]
    tab.start()
    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)
    yield connection


@pytest.fixture(scope='session')
def connection_with_simulating_traffic(connection):
    dev_tools = pychrome.Browser(url="http://localhost:8000")
    tab = dev_tools.list_tab()[0]
    tab.start()
    tab.call_method("Network.emulateNetworkConditions",
                     offline=False,
                     latency=100,
                     downloadThroughput=93750,
                     uploadThroughput=31250,
                     connectionType="wifi")

    tab.call_method("Network.enable", _timeout=20)

    yield connection
