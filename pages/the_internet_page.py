from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class TheInternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com"
    DYNAMIC_LOADING_START = (By.CSS_SELECTOR, "#start button")
    DYNAMIC_LOADING_RESULT = (By.CSS_SELECTOR, "#finish h4")

    def open_dynamic_loading(self):
        self.driver.get(f"{self.URL}/dynamic_loading/2")
        self.wait.until(EC.element_to_be_clickable(self.DYNAMIC_LOADING_START))

    def has_dynamic_loading_result(self):
        return bool(self.driver.find_elements(*self.DYNAMIC_LOADING_RESULT))

    def start_dynamic_loading(self):
        self.wait.until(EC.element_to_be_clickable(self.DYNAMIC_LOADING_START)).click()

    def wait_for_dynamic_loading_result(self):
        result = self.wait.until(EC.visibility_of_element_located(self.DYNAMIC_LOADING_RESULT))
        return result.text

    def get_feature_links(self):
        links = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content ul li a"))
        )
        return {link.text: link for link in links}
