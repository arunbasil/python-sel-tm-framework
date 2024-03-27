
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from base.base_driver import BaseDriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from utilities.logger import setup_logger


class PropertySearchResultsPage(BaseDriver):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.logger = setup_logger("PropertySearchResultsPage")

    # DECLARE WEB ELEMENTS------------------------------------------------
    PROPERTY_TITLE_TEXT = "Residential properties | Trade Me Property"
    PROPERTY_SEARCH_HEADER = (By.XPATH, "//tm-property-search-header/div/div/tm-search-header-heading/h1")
    PROPERTY_SEARCH_RESULTS_HEADER = (
        By.XPATH, "//tm-property-search-results[1]/div[1]/div[2]/tm-search-header-result-count[1]/h3[1]")
    PAGINATION_TEXT = (By.XPATH, "//tm-property-search-results//tg-pagination//ul")
    PAGINATION_CONTAINER_XPATH = (By.XPATH, "//tg-pagination//ul")
    PAGINATION_LINKS_XPATH = (By.XPATH, "//tg-pagination-link")
    # SEARCH_RESULTS_LIST = (
    #     By.XPATH, "//tm-property-search-component//tm-property-search-results//tm-search-results//tg-row")
    SEARCH_RESULTS_LIST = (By.CSS_SELECTOR, "tg-col[flexcontents='true']")

    # ---LISTING ELEMENTS---
    LISTING_TITLE = (By.XPATH, "//tm-property-search-card-listing-title[contains(@id, 'title')]")
    LISTING_ADDRESS = (By.XPATH, "//tm-property-search-card-address-subtitle[contains(@id, 'subtitle')]")

    # PAGINATION
    PAGINATION_LINKS = (By.XPATH,
                        "//tm-property-search-component//tm-property-search-results//tm-search-results//tg-pagination//ul//tg-pagination-link/a[@class='ng-star-inserted']")
    PAGINATION_NEXT_BUTTON = (By.XPATH, "//a[starts-with(@aria-label, 'Next page')]")

    def property_search_results_page_title(self):
        # return self.get_page_title()
        return self.wait_for_page_load(self.PROPERTY_TITLE_TEXT)

    def property_search_header(self) -> str:
        return self.wait_for_element_presence(self.PROPERTY_SEARCH_HEADER).text

    def get_number_of_search_results(self) -> str:
        return self.wait_for_element_presence(self.PROPERTY_SEARCH_RESULTS_HEADER).text

    def get_pagination_page_nos(self) -> list:
        return self.get_number_of_pages(self.PAGINATION_TEXT)

    def get_search_results(self):
        return self.wait_for_elements_present(self.SEARCH_RESULTS_LIST)

    def get_search_results_list(self) -> list[dict]:
        search_results = []
        try:
            title_elements = self.wait_for_elements_present(self.LISTING_TITLE)
            address_elements = self.wait_for_elements_present(self.LISTING_ADDRESS)
            if len(title_elements) != len(address_elements):
                raise ValueError("Mismatch in the number of titles and addresses found.")
            for title, address in zip(title_elements, address_elements):
                search_result = {
                    "title": title.text if title else None,
                    "address": address.text if address else None
                }
                search_results.append(search_result)
        except StaleElementReferenceException:
            title_elements = self.wait_for_elements_present(self.LISTING_TITLE)
            address_elements = self.wait_for_elements_present(self.LISTING_ADDRESS)
            if len(title_elements) != len(address_elements):
                raise ValueError("Mismatch in the number of titles and addresses found.")
            for title, address in zip(title_elements, address_elements):
                search_result = {
                    "title": title.text if title else None,
                    "address": address.text if address else None
                }
                search_results.append(search_result)
        return search_results

    def get_all_search_results_from_all_resulted_pages(self) -> list[dict]:
        all_search_results = []
        current_page = 1

        while True:
            # Collect search results from the current page
            search_results = self.get_search_results_list()
            all_search_results.extend(search_results)

            # Try to find the next page button; if it's not found or disabled, break the loop
            next_page_buttons = self.wait_for_element_clickable(self.PAGINATION_TEXT)
            print(next_page_buttons.get_attribute("class"))
            if not next_page_buttons or "disabled-class-name" in next_page_buttons.get_attribute("class"):
                break

            # # Click the next page button and wait for the page to load
            # next_page_buttons[-1].click()
            # self.wait_for_page_load(current_page + 1)
            # current_page += 1

        return all_search_results

    def get_all_search_results_from_all_resulted_pages_v1(self):
        # Find the pagination container
        pagination_container = self.wait_for_elements_present(self.PAGINATION_CONTAINER_XPATH)
        # Find all pagination links within the container
        pagination_links = self.wait_for_elements_present(self.PAGINATION_LINKS_XPATH)
        all_search_results = []

        for link in pagination_links:
            print(link.text)

    def go_to_page(self, page_number):
        # Assuming page_number is 1-indexed
        pagination_links = self.wait_for_elements_present(self.PAGINATION_LINKS)
        if page_number <= len(pagination_links) and page_number > 0:
            # Click the pagination link corresponding to the page_number
            pagination_links[page_number - 1].click()
        else:
            print(f"Page number {page_number} is out of range.")

    # def collect_search_results_from_all_pages(self):
    #     all_results = []
    #     current_page = 1
    #     while True:
    #         print(f"Collecting results from page {current_page}")
    #         page_results = self.get_search_results_list()
    #         all_results.extend(page_results)
    #         print(f"Total results collected so far: {len(all_results)}")
    #
    #         try:
    #             next_button = self.wait_for_element_visible(self.PAGINATION_NEXT_BUTTON)
    #             if next_button:
    #                 print("Next button found and clickable. Moving to the next page.")
    #                 next_button.click()
    #                 sleep(5)  # Adjust sleep time based on your page's load time
    #                 current_page += 1
    #             else:
    #                 print("Next button not found or not clickable. Ending the loop.")
    #                 break
    #         except TimeoutException:
    #             print("TimeoutException: Next button not clickable within 2 seconds. Ending the loop.")
    #             break
    #
    #     return all_results

    def is_next_button_clickable(self):
        """Check if the Next button is present and clickable."""
        try:
            return self.wait_for_element_visible(self.PAGINATION_NEXT_BUTTON, 20)
        except TimeoutException:
            print("Next button not clickable within the specified timeout.")
            return None

    def navigate_to_next_page(self):
        """Click the Next button to go to the next page."""
        next_button = self.is_next_button_clickable()
        if next_button:
            next_button.click()
            return True
        return False

    def collect_search_results_from_all_pages(self) -> list[dict]:
        """Collect search results from all pages."""
        all_results = []
        current_page = 1

        while True:
            self.logger.info(f"Collecting results from page {current_page}")
            page_results = self.get_search_results_list()
            all_results.extend(page_results)
            self.logger.info(f"Total results collected so far: {len(all_results)}")

            if not self.navigate_to_next_page():
                self.logger.info("No more pages to navigate. Ending the loop.")
                break

            current_page += 1
        # return List of dicts
        return all_results
