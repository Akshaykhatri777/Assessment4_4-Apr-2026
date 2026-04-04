import pytest
from selenium import webdriver
from config.env import ConfigReader

@pytest.fixture
def setup_and_teardown():
    # Read config
    config = ConfigReader.read_config()
    env = config['qa']
    base_url = env['base_url']
    # Setup (Before Test)
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver      # Test Runs Here
    # Teardown - after test
    driver.quit()