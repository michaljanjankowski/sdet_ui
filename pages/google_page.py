from enum import Enum
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from .base_page import BasePage, LocatorStorage


class GoogleLocators(Enum):
    QueryInputField = LocatorStorage(locator=By.NAME, value="q")
    ResultsIdentyty = LocatorStorage(locator=By.ID, value="result-stats")


class GoogleSearchBlockedError(RuntimeError):
    """Google requires manual verification instead of serving search results."""


class GooglePage(BasePage):
    URL = "https://www.google.com/?hl=en"

    RESULTS = (By.CSS_SELECTOR, "#search a:has(h3)")

    def ask_google_about_text_and_wait_for_results(self, text: str):
        self.dismiss_cookie_consent()
        search_box = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys(text, Keys.RETURN)
        self.wait.until(
            lambda driver: (
                urlparse(driver.current_url).path == "/search"
                or urlparse(driver.current_url).path.startswith("/sorry/")
            )
        )
        self.get_search_results()

    def get_search_results(self):
        def results_or_block(driver):
            if urlparse(driver.current_url).path.startswith("/sorry/"):
                raise GoogleSearchBlockedError(
                    "Google blocked automated search with CAPTCHA/unusual traffic verification."
                )
            return expected_conditions.visibility_of_any_elements_located(self.RESULTS)(driver)

        return self.wait.until(results_or_block)
