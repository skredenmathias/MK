# add this in the conftest.py under tests folder
from selenium.webdriver.chrome.options import Options

def pytest_setup_options():
    options = Options()
    options.add_argument('--disable-gpu')
    return options