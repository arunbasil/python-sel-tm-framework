from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from typing import Tuple, Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BaseDriver():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_page_load(self, expected_title: str, timeout: int = 10) -> str:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: expected_title in driver.title
            )
            print(f"Page loaded successfully with title: {self.driver.title}")
            return self.driver.title
        except TimeoutException:
            error_message = f"Page load timeout: Expected title not found within {timeout} seconds"
            print(error_message)
            return error_message  # Return the error message as a string instead of False

    def wait_for_element(self, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} not found within {timeout} seconds")
            return None

    def wait_for_element_clickable(self, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
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

    def get_page_title(self, timeout=10) -> str:
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(self.driver.title))
            print(f"Page loaded successfully with title: {self.driver.title}")
            return self.driver.title
        except TimeoutException:
            error_msg = f"Page load timeout: {timeout} seconds"
            print(error_msg)
            return error_msg

    def get_current_page_results(self, result_selector):
        results = self.driver.find_elements_by_css_selector(result_selector)
        return [result.text for result in results]

    def is_next_page_available(self, next_page_selector):
        next_page_button = self.driver.find_elements_by_css_selector(next_page_selector)
        return len(next_page_button) != 0 and next_page_button[0].is_displayed()

    def go_to_next_page(self, next_page_selector):
        next_page_button = self.driver.find_element_by_css_selector(next_page_selector)
        if next_page_button.is_displayed():
            next_page_button.click()
            # Add wait for the page to load if necessary

    def get_number_of_pages(self, element: tuple):
        pagination_text = self.wait_for_element(element).text
        # Convert the string into a list, filtering out non-integer values
        pagination_list = [item for item in pagination_text.strip().split('\n') if item.isdigit()]
        # Convert list items to integers
        return list(map(int, pagination_list))

    def wait_for_elements_present(self, locator: tuple, timeout: int = 10, parent: WebElement = None) -> list[
        WebElement]:
        """Wait for all elements that match a locator to be present in the DOM."""
        parent = parent or self.driver
        try:
            return WebDriverWait(parent, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Elements not found with locator: {locator}")
