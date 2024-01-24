from .base_page import BasePage, LocatorStorage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from enum import Enum


class GoogleLocators(Enum):
    QueryInputField = LocatorStorage(locator=By.NAME, value="q")
    ResultsIdentyty = LocatorStorage(locator=By.ID, value="result-stats")


class GooglePage(BasePage):

    def ask_google_about_text_and_wait_for_results(self, text: str):
        search_box_web = self.driver.find_element(By.NAME, "q")
        search_box_web.send_keys(text)
        search_box_web.send_keys(Keys.RETURN)
        ignored_exceptions = ( StaleElementReferenceException,)
        self._seartch_results_wel = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.TAG_NAME, "body")))

    def get_search_results(self):
        all_divs = self._seartch_results_wel.find_elements(By.XPATH, "//div[contains(@class, 'yuRUbf')]")
        assert all_divs
