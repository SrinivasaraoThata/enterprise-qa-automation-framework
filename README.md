# Enterprise QA Automation Framework

This repository contains a robust QA automation framework built to simulate real-world enterprise testing scenarios. It is designed with modularity, scalability, and maintainability in mind.

## 🚀 Key Features

- **UI Automation**: Built with Python and Selenium 4.
- **Page Object Model (POM)**: Ensures clean separation between test logic and UI elements.
- **Auto-managed Drivers**: Uses Selenium Manager (integrated in Selenium 4) for seamless browser driver management.
- **Configuration Management**: Centralized YAML-based configuration for URLs, credentials, and timeouts.
- **Rich Logging**: Integrated logging system for better debugging and traceability.
- **Headless Execution**: Configured for both headed and headless browser execution.

## 📁 Project Structure

- `src/pages/`: Contains Page Object classes representing web pages.
- `src/utils/`: Utility classes for logging, configuration loading, etc.
- `tests/ui/`: Contains UI-specific test cases using `pytest`.
- `config/`: YAML configuration files.

## 🛠️ Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SrinivasaraoThata/enterprise-qa-automation-framework.git
   cd enterprise-qa-automation-framework
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

To run all UI tests:
```bash
pytest tests/ui/test_login.py -v
```

To run tests in headless mode (default in current config):
```bash
pytest tests/ui/test_login.py
```

## 📝 Recent Improvements
- Fixed Environment setup and missing dependencies.
- Resolved browser driver compatibility issues (WinError 193).
- Updated locators for both alert-level and field-level validation errors.
- Improved framework stability with dynamic timeouts and headless support.

---
*This is a generic learning project inspired by enterprise automation practices. No proprietary systems or data are used.*