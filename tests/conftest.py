from pathlib import Path

import pytest

from pages.google_page import GooglePage
from pages.the_internet_page import TheInternetPage
from pages.youtube_page import YouTubePage


@pytest.fixture
def google_page(driver):
    driver.get(GooglePage.URL)
    return GooglePage(driver)


@pytest.fixture
def youtube_page(driver):
    driver.get(YouTubePage.URL)
    return YouTubePage(driver)


@pytest.fixture
def the_internet_page(driver):
    driver.get(TheInternetPage.URL)
    return TheInternetPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed or "driver" not in item.funcargs:
        return

    driver = item.funcargs["driver"]
    artifact_dir = Path("test-results")
    artifact_dir.mkdir(exist_ok=True)
    test_name = item.nodeid.replace("/", "_").replace("::", "__")
    driver.save_screenshot(artifact_dir / f"{test_name}.png")
    (artifact_dir / f"{test_name}.html").write_text(driver.page_source, encoding="utf-8")
