import pytest

from pages.google_page import GooglePage
from pages.the_internet_page import TheInternetPage
from pages.youtube_page import YouTubePage


@pytest.fixture
def google_page_ssn(connection):
    connection.get(GooglePage.URL)
    yield connection


@pytest.fixture
def enter_youtube_page(connection):
    connection.get(YouTubePage.URL)
    yield connection


@pytest.fixture
def enter_theinternet_page(connection):
    connection.get(TheInternetPage.URL)
    yield connection
