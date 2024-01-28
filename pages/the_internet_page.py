from .base_page import BasePage, LocatorStorage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from enum import Enum


class TheInternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com"

    def _get_all_featurs_and_store_to_dct(self):
        all_features_wel_lst = self.driver.find_elements(By.XPATH, "//div[contains(@id, 'content')]/ul/*")
        self.features_dct = {wel.text:wel for wel in all_features_wel_lst}


