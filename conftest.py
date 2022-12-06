import pytest
from selene.support.shared import browser
from selene import command, have

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1600
    browser.config.window_height = 900
    #browser.all('[id^=google_ads_iframe_][id$=__container__]').should(have.size_greater_than_or_equal(3)).perform(command.js.remove)
    yield
    browser.quit()