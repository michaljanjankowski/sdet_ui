from urllib.parse import parse_qs, urlparse

import pytest

from pages.google_page import GooglePage, GoogleSearchBlockedError
from pages.youtube_page import YouTubePage


def test_search_for_results_and_check(google_page_ssn) -> None:
    google_page = GooglePage(driver=google_page_ssn)
    try:
        google_page.ask_google_about_text_and_wait_for_results(text="Python")
    except GoogleSearchBlockedError as error:
        pytest.skip(str(error))
    google_page.scroll_to_bottom()
    assert google_page.get_search_results()
    assert parse_qs(urlparse(google_page_ssn.current_url).query)["q"] == ["Python"]


def test_another(enter_youtube_page) -> None:
    youtube_page = YouTubePage(driver=enter_youtube_page)
    assert youtube_page.search("Grandfather day")
    assert parse_qs(urlparse(enter_youtube_page.current_url).query)["search_query"] == [
        "Grandfather day"
    ]
