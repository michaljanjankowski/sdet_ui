from urllib.parse import parse_qs, urlparse

import pytest

from pages.google_page import GoogleSearchBlockedError


def test_google_search_returns_results(google_page, driver) -> None:
    try:
        google_page.ask_google_about_text_and_wait_for_results(text="Python")
    except GoogleSearchBlockedError as error:
        pytest.skip(str(error))
    google_page.scroll_to_bottom()
    assert google_page.get_search_results()
    assert parse_qs(urlparse(driver.current_url).query)["q"] == ["Python"]


def test_youtube_search_returns_videos(youtube_page, driver) -> None:
    assert youtube_page.search("Grandfather day")
    assert parse_qs(urlparse(driver.current_url).query)["search_query"] == ["Grandfather day"]
