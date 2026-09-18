from pages.the_internet_page import TheInternetPage


def test_home_page_contains_checkbox_link(the_internet_page):
    features = the_internet_page.get_feature_links()
    assert "Checkboxes" in features
    assert features["Checkboxes"].get_attribute("href") == f"{TheInternetPage.URL}/checkboxes"


def test_dynamic_loading_renders_result_after_start(the_internet_page):
    the_internet_page.open_dynamic_loading()

    assert not the_internet_page.has_dynamic_loading_result(), (
        "Result should not exist in initial DOM"
    )

    the_internet_page.start_dynamic_loading()

    assert the_internet_page.wait_for_dynamic_loading_result() == "Hello World!"
