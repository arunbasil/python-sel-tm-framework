from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.base_driver import BaseDriver


class MotorsResultsPage(BaseDriver):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, ".tm-search-header-result-count__heading.ng-star-inserted")

    def get_search_results_header_text(self) -> str:
        """
        Returns the TEXT (element.text) of the search results header element
        """
        # element = self.driver.find_element(*self.results_header)
        # return element.text
        return self.wait_for_element(self.SEARCH_RESULTS_HEADER).text
    def get_property_search_results_page_title(self):
        return self.get_page_title()

