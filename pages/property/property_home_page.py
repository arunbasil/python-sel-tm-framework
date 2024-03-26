from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver

'''
Property Search Results page
'''


class PropertyHomePage(BaseDriver):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, ".tm-search-header-result-count__heading.ng-star-inserted")
    RESULTS_SELECTOR = (By.XPATH, "")

    def get_search_results_header_text(self) -> str:
        """
        Returns the TEXT (element.text) of the search results header element
        """
        return self.wait_for_element_presence(self.SEARCH_RESULTS_HEADER).text

    def get_property_search_results_page_title(self) -> str:
        return self.get_page_title()

    def get_current_page_results(self):
        # Find all elements that represent individual search results.
        # Replace 'result_selector' with the actual selector for search results.
        results: list[WebElement] = self.driver.find_elements(self.RESULTS_SELECTOR)
        return [result.text for result in results]  # Or any other relevant data from the result element.

    def is_next_page_available(self):
        # Replace 'next_page_selector' with the actual selector for the next page button or link.
        next_page_button = self.driver.find_elements_by_css_selector('next_page_selector')
        return len(next_page_button) != 0 and next_page_button[0].is_displayed()

    def go_to_next_page(self):
        # Replace 'next_page_selector' with the actual selector for the next page button or link.
        next_page_button = self.driver.find_element_by_css_selector('next_page_selector')
        if next_page_button.is_displayed():
            next_page_button.click()
            # Wait for the page to load, e.g., wait for a specific element that signifies the page has loaded.
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(('css_selector', 'some_element_that_signifies_page_loaded'))
            )

    def get_all_results_across_pages(self):
        all_results = []
        while True:
            all_results.extend(self.get_current_page_results())
            if self.is_next_page_available():
                self.go_to_next_page()
            else:
                break
        return all_results
