import pytest
from selene.support.shared import browser
from selene import command, have

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
    browser.all('[id^=google_ads_iframe_][id$=__container__]').should(have.size_greater_than_or_equal(3)).perform(command.js.remove)
    b = browser.open('https://demoqa.com/automation-practice-form')
    yield b
    browser.quit()