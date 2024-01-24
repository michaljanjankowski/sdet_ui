from pages.google_page import GooglePage
from selenium.webdriver.common.by import By


def test_search_for_results_and_check(google_page_ssn) -> None:
    google_page = GooglePage(driver=google_page_ssn)
    google_page.ask_google_about_text_and_wait_for_results(text='Python')
    google_page.scroll_to_bottom()
    google_page.get_search_results()
    assert True


def test_another(enter_youtube_page) -> None:
    serch_bar_wel = enter_youtube_page.find_element(By.XPATH, '//input[@id="search"]')
    serch_bar_wel.send_keys('Gradfather day')
    button_wel = enter_youtube_page.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
    button_wel.click()
    results_parent_wel = enter_youtube_page.find_element(By.XPATH, '//div[@id="contents"]')
    serchresults = results_parent_wel.find_elements(By.XPATH, '//ytd-video-renderer/*')
    assert len(serchresults)

