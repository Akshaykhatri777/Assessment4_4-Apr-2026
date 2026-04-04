from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger


def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown

    lp = LoginPage(driver)

    config = ConfigReader.read_config()
    env = config['qa']

    BASE_URL = env['base_url']
    USERNAME = env['username']
    PASSWORD = env['passwd']

    # Open the website
    driver.get(BASE_URL)

    # Log intention (useful when debugging test runs later)
    get_logger().info("Trying to Log In")

    # Perform login
    lp.click_login()
    lp.enter_email(USERNAME)
    lp.enter_password(PASSWORD)
    lp.click_login_button()