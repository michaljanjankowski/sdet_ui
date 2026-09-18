from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class YouTubePage(BasePage):
    URL = "https://www.youtube.com/?hl=en"
    RESULTS = (By.CSS_SELECTOR, "ytd-video-renderer a#video-title")

    def search(self, text: str):
        self.dismiss_cookie_consent()
        search_box = self.wait.until(EC.element_to_be_clickable((By.NAME, "search_query")))
        search_box.clear()
        search_box.send_keys(text, Keys.RETURN)
        self.wait.until(EC.url_contains("/results?search_query="))
        return self.wait.until(EC.visibility_of_any_elements_located(self.RESULTS))
