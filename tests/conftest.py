import pytest
from pages.google_page import GooglePage
from pages.the_internet_page import TheInternetPage


@pytest.fixture(scope='session')
def google_page_ssn(connection):
    connection.get(GooglePage.URL)
    yield connection


@pytest.fixture(scope='session')
def enter_youtube_page(connection):
    connection.get("https://www.youtube.com")
    yield connection


@pytest.fixture(scope='session')
def enter_theinternet_page(connection):
    connection.get(TheInternetPage.URL)
    yield connection