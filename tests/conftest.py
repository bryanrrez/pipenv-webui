"""
This module contains shared fixtures for web UI tests.
 """

import pytest
import json

from selenium import webdriver


CONFIG_PATH = 'tests/config.json'
DEFAUTL_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    # Read the jSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
        return data

@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contains "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception('{browser} is not a supported browser'.format(browser=config['browser']))
    else:
        return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    if  'wait_time' not in config:
        return DEFAUTL_WAIT_TIME

    return config['wait_time'] 

@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = webdriver.Chrome()
    elif config_browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception('{config_browser} is not a supported browser'.format(config_browser=config_browser))

    # Wait implicitly for elements to be ready before atteting interactions
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver
    
    # For cleanup, quit the driver
    driver.quit()