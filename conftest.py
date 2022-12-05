import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
    b = browser.open('https://demoqa.com/automation-practice-form')
    yield b
    browser.quit()