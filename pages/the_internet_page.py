from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class TheInternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com"

    def get_all_featurs_and_store_to_dct(self):
        links = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content ul li a"))
        )
        self.features_dct = {link.text: link for link in links}
        return self.features_dct
