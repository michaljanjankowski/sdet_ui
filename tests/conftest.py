import pytest


@pytest.fixture(scope='session')
def google_page_ssn(connection):
    connection.get("https://www.google.com")
    yield connection


@pytest.fixture(scope='session')
def enter_youtube_page(connection):
    connection.get("https://www.youtube.com")
    yield connection