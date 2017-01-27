import tkinter

import pytest

from selene import factory
from selene.browsers import Browser
from selene.tools import get_driver, set_driver
from tests.acceptance.helpers.helper import get_test_driver


@pytest.mark.parametrize("browser_name", ["firefox",
                                          "chrome"])
def test_factory_can_start_browser_maximized(browser_name):
    driver = factory._start_driver(browser_name)
    assert driver.name == browser_name


@pytest.mark.parametrize("browser_name", ["firefox",
                                          "chrome"])
def test_factory_can_create_browser(browser_name):
    factory.ensure_driver_started(browser_name)
    assert get_driver().name == browser_name


def test_can_set_browser_directly():
    driver = get_test_driver()
    set_driver(driver)
    factory.ensure_driver_started(Browser.CHROME)
    assert get_driver().name == Browser.CHROME
    get_driver().quit()
    driver.quit()
