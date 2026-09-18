from dataclasses import dataclass

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


@dataclass
class LocatorStorage:
    locator: By
    value: str


class BasePage(PageFactory):
    URL = ""
    locators = {}

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def dismiss_cookie_consent(self):
        reject_button = (
            By.XPATH,
            "//button[normalize-space(.)='Reject all' or "
            "normalize-space(.)='Odrzuć wszystko' or "
            ".//*[normalize-space(.)='Reject all' or normalize-space(.)='Odrzuć wszystko']]",
        )
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(reject_button))
        except TimeoutException:
            return

        def dismiss_when_ready(driver):
            if EC.invisibility_of_element_located(reject_button)(driver):
                return True
            ready_button = EC.element_to_be_clickable(reject_button)(driver)
            if ready_button:
                ready_button.click()
            return False

        # Consent controls can appear before their JavaScript handlers are ready.
        WebDriverWait(
            self.driver,
            20,
            poll_frequency=1,
            ignored_exceptions=(StaleElementReferenceException, ElementClickInterceptedException),
        ).until(dismiss_when_ready)
