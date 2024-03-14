from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException,ElementNotInteractableException
from typing import Tuple,Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BaseDriver():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_page_load(driver: WebDriver, expected_title: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(driver, timeout).until(
                lambda driver: expected_title in driver.title
            )
            print(f"Page loaded successfully with title: {driver.title}")
            return True
        except TimeoutException:
            print(f"Page load timeout: Expected title not found within {timeout} seconds")
            return False
        
    def wait_for_element_clickable(self,locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Element {locator} not clickable within {timeout} seconds")
            return None
    
    def enter_text(self, locator: WebElement, text: str):
        try:
            search_input = locator
            search_input.clear()
            search_input.send_keys(text)
        except TimeoutException:
            print(f"Timed out waiting for element with locator {locator} to be clickable.")
        except NoSuchElementException:
            print(f"Element with locator {locator} could not be found.")
        except ElementNotInteractableException:
            print(f"Element with locator {locator} could not be interacted with.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")