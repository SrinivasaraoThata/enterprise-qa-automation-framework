from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_loader import load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)
config = load_config()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get('explicit_wait', 10))

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        logger.info(f"Typing '{text}' into element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        logger.info(f"Checking if element is displayed: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False