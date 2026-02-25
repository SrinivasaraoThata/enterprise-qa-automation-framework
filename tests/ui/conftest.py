import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.config_loader import load_config

@pytest.fixture()
def driver():
    config = load_config()
    
    # Setup — opens browser
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(config['urls']['base_url'])
    
    yield driver  # hands browser to the test
    
    # Teardown — closes browser
    driver.quit()