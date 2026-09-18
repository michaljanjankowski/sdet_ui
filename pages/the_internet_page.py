from selenium.webdriver.common.by import By

from .base_page import BasePage


class TheInternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com"

    def _get_all_featurs_and_store_to_dct(self):
        all_features_wel_lst = self.driver.find_elements(
            By.XPATH, "//div[contains(@id, 'content')]/ul/*"
        )
        self.features_dct = {wel.text: wel for wel in all_features_wel_lst}
