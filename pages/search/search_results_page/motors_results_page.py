from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.base_driver import BaseDriver


class MotorsResultsPage(BaseDriver):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    RESULT_ITEMS = (By.CSS_SELECTOR, "div.tm-motors-search-listing__result")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "a[rel='next']")
    SORT_DROPDOWN = (By.ID, "sorting-dropdown")
    SEARCH_RESULTS_HEADER = (By.XPATH, "//tm-search-header-result-count/h3")

    def get_search_results_header_text(self) -> str:
        """
        Returns the TEXT (element.text) of the search results header element
        """
        # element = self.driver.find_element(*self.results_header)
        # return element.text
        return self.wait_for_element_presence(self.SEARCH_RESULTS_HEADER).text

    def is_keyword_in_results_header(self, keyword: str) -> bool:
        header_text = self.get_search_results_header_text()
        return keyword in header_text

    def get_result_items(self) -> List[WebElement]:
        return self.driver.find_elements(*self.result_items)

    def go_to_next_page(self):
        next_button = self.driver.find_element(*self.pagination_next)
        if next_button:
            next_button.click()

    def select_sorting_option(self, option_value: str):
        dropdown = self.driver.find_element(*self.sorting_dropdown)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == option_value:
                option.click()
                break

    def get_motor_results_page_title(self, expected_title):
        return self.wait_for_page_load(expected_title)
