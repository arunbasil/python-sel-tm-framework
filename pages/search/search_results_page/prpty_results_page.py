from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from base.base_driver import BaseDriver


class PropertySearchResultsPage(BaseDriver):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def get_number_of_search_results(self):
        # Implement logic to return the number of search results
        return len(self.driver.find_elements_by_css_selector("your-result-selector"))
