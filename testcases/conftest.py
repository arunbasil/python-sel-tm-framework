import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # elif browser_name == "edge":
    #     driver = webdriver.Edge(service=EdgeService(EdgeDriverManager().install()))
    # elif browser_name == "safari" and platform.system() == 'Darwin':  # Safari is only available on macOS
    #     driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get("https://www.trademe.co.nz/")
    driver.maximize_window()
    yield driver
    driver.quit()
