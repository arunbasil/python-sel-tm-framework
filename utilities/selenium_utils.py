# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webdriver import WebDriver
# from typing import Tuple,Optional
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.remote.webelement import WebElement

# class Utils():
#     @staticmethod
#     def wait_for_page_load(driver: WebDriver, expected_title: str, timeout: int = 10) -> bool:
#         try:
#             WebDriverWait(driver, timeout).until(
#                 lambda driver: expected_title in driver.title
#             )
#             print(f"Page loaded successfully with title: {driver.title}")
#             return True
#         except TimeoutException:
#             print(f"Page load timeout: Expected title not found within {timeout} seconds")
#             return False


    # @staticmethod
    # def wait_for_element(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
    #     try:
    #         return WebDriverWait(driver, timeout).until(
    #             EC.presence_of_element_located(locator)
    #         )
    #     except TimeoutException:
    #         print(f"Element {locator} not found within {timeout} seconds")
    #         return None
        
    # @staticmethod
    # def wait_for_element_clickable(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
    #     try:
    #         return WebDriverWait(driver, timeout).until(
    #             EC.element_to_be_clickable(locator)
    #         )
    #     except TimeoutException:
    #         print(f"Element {locator} not clickable within {timeout} seconds")
    #         return None
    # @staticmethod
    # def wait_for_element_visible(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebElement]:
    #     """Waits for an element to be present on the DOM of a page and visible."""
    #     try:
    #         return WebDriverWait(driver, timeout).until(
    #             EC.visibility_of_element_located(locator)
    #         )
    #     except TimeoutException:
    #         print(f"Element {locator} not visible within {timeout} seconds")
    #         return None

    # @staticmethod
    # def wait_for_element_to_disappear(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> bool:
    #     try:
    #         return WebDriverWait(driver, timeout).until_not(
    #             EC.presence_of_element_located(locator)
    #         )
    #     except TimeoutException:
    #         print(f"Element {locator} still present after {timeout} seconds")
    #         return False
    # @staticmethod
    # def switch_to_new_window(driver: WebDriver, timeout: int = 10):
    #     """
    #     Switches to the newly opened window/tab.

    #     :param driver: WebDriver instance.
    #     :param timeout: Time in seconds to wait for the new window/tab to appear.
    #     """
    #     original_window = driver.current_window_handle
    #     try:
    #         # Wait until a new window or tab is opened.
    #         WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > 1)
            
    #         # Get the list of all window handles available to the session.
    #         available_windows = driver.window_handles
            
    #         # Switch to the new window. This assumes that the new window is the last one in the list.
    #         new_window = next(window for window in available_windows if window != original_window)
    #         driver.switch_to.window(new_window)
    #     except TimeoutException:
    #         print(f"No new window/tab appeared within {timeout} seconds.")

    # @staticmethod
    # def scroll_to_bottom(driver: WebDriver):
    #     """
    #     Scrolls the web page to the bottom.

    #     :param driver: WebDriver instance.
    #     """
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # @staticmethod
    # def scroll_to_top(driver: WebDriver):
    #     """
    #     Scrolls the web page to the top.

    #     :param driver: WebDriver instance.
    #     """
    #     driver.execute_script("window.scrollTo(0, 0);")

    # @staticmethod
    # def scroll_to_element(driver: WebDriver, element):
    #     """
    #     Scrolls the web page to bring the specified element into view.

    #     :param driver: WebDriver instance.
    #     :param element: The web element to scroll into view.
    #     """
    #     driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # @staticmethod
    # def scroll_by_amount(driver: WebDriver, x_pixels, y_pixels):
    #     """
    #     Scrolls the web page by the specified amount of pixels.

    #     :param driver: WebDriver instance.
    #     :param x_pixels: The number of pixels to scroll horizontally.
    #     :param y_pixels: The number of pixels to scroll vertically.
    #     """
    #     driver.execute_script(f"window.scrollBy({x_pixels}, {y_pixels});")

