from pages.the_internet_page import TheInternetPage


def test_enter_theinternet_page_and_get_all_links(enter_theinternet_page):
    the_inet_page = TheInternetPage(driver=enter_theinternet_page)
    features = the_inet_page.get_all_featurs_and_store_to_dct()
    assert "Checkboxes" in features
    assert features["Checkboxes"].get_attribute("href") == f"{TheInternetPage.URL}/checkboxes"


def test_dynamic_loading_renders_result_after_start(connection):
    page = TheInternetPage(driver=connection)
    page.open_dynamic_loading()

    assert not page.has_dynamic_loading_result(), "Result should not exist in the initial DOM"

    page.start_dynamic_loading()

    assert page.wait_for_dynamic_loading_result() == "Hello World!"
