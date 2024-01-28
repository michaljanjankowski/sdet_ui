from pages.the_internet_page import TheInternetPage
from selenium.webdriver.common.by import By


def test_enter_theinternet_page_and_get_all_links(enter_theinternet_page):
    the_inet_page = TheInternetPage(driver=enter_theinternet_page)
    the_inet_page.get_all_featurs_and_store_to_dct()
    assert True