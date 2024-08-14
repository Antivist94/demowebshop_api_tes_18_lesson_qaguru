import pytest
from selene import browser, have


@pytest.fixture
def base_url():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    return 'https://demowebshop.tricentis.com'
