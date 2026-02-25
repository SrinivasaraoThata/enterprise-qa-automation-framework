import pytest
from src.pages.login_page import LoginPage
from src.utils.config_loader import load_config

config = load_config()

class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login(
            config['credentials']['username'],
            config['credentials']['password']
        )
        assert login_page.is_dashboard_displayed(), "Dashboard should be visible after valid login"

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.login(
            config['credentials']['username'],
            "wrongpassword"
        )
        error = login_page.get_error_message()
        assert "Invalid credentials" in error, "Error message should appear for wrong password"

    def test_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.login("", "")
        error = login_page.get_error_message()
        assert "Required" in error, "Error message should appear for empty credentials"