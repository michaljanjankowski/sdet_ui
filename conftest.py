import pychrome
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run Chrome without opening a visible window.",
    )


@pytest.fixture
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=0")
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(0)
    driver.set_page_load_timeout(45)
    if not request.config.getoption("--headless"):
        driver.maximize_window()

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def connection_with_capturing_network_traffic(driver):

    def output_on_start(**kwargs):
        print(f"START {kwargs}")

    def output_on_end(**kwargs):
        print(f"FINISHED {kwargs}")

    debugger_address = driver.capabilities["goog:chromeOptions"]["debuggerAddress"]
    dev_tools = pychrome.Browser(url=f"http://{debugger_address}")
    tab = dev_tools.list_tab()[0]
    tab.start()
    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)
    yield driver
    tab.stop()


@pytest.fixture
def connection_with_simulating_traffic(driver):
    debugger_address = driver.capabilities["goog:chromeOptions"]["debuggerAddress"]
    dev_tools = pychrome.Browser(url=f"http://{debugger_address}")
    tab = dev_tools.list_tab()[0]
    tab.start()
    tab.call_method(
        "Network.emulateNetworkConditions",
        offline=False,
        latency=100,
        downloadThroughput=93750,
        uploadThroughput=31250,
        connectionType="wifi",
    )

    tab.call_method("Network.enable", _timeout=20)

    yield driver
    tab.stop()
