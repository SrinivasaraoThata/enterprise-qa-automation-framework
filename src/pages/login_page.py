from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    FIELD_ERROR = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def login(self, username, password):
        logger.info(f"Logging in with username: {username}")
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_field_error_message(self):
        return self.get_text(self.FIELD_ERROR)

    def is_dashboard_displayed(self):
        return self.is_displayed(self.DASHBOARD_HEADER)