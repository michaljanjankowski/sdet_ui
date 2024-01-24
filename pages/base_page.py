from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class LocatorStorage():
    locator: By
    value: str


class BasePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
