import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def driver_setting():
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
