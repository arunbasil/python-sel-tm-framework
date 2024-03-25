from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from base.base_driver import BaseDriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class PropertySearchResultsPage(BaseDriver):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

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

    def property_search_results_page_title(self):
        # return self.get_page_title()
        return self.wait_for_page_load(self.PROPERTY_TITLE_TEXT)

    def property_search_header(self) -> str:
        return self.wait_for_element(self.PROPERTY_SEARCH_HEADER).text

    def get_number_of_search_results(self) -> str:
        return self.wait_for_element(self.PROPERTY_SEARCH_RESULTS_HEADER).text

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
        except NoSuchElementException as e:
            print(f"An Listing element was not found: {e}")
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



        # try:
        #     while True:
        #         # Process the current page's listings here...
        #         search_results = self.get_search_results_list()
        #         all_search_results.extend(search_results)
        #
        #         # Find the next button. This is usually the last button in the pagination container.
        #         # We use try/except to handle the case where the next button might not be present on the last page.
        #         try:
        #             # next_button = [link for link in pagination_links if 'Next' in link.text][0]
        #             print(next_button.text)
        #         except IndexError:
        #             print("No 'Next' button found. Assuming we are on the last page.")
        #             break  # Exit the loop if we are on the last page
        #
        #         # Check if the next button is enabled or disabled.
        #         if 'disabled-class-name' in next_button.get_attribute("class"):
        #             print("Next button is disabled. We are on the last page.")
        #             break  # Stop if the next button is disabled (we are on the last page)
        #         else:
        #             next_button.click()  # Click the next button to go to the next page
        #
        # except NoSuchElementException:
        #     print("Pagination structure is different or cannot be found.")
        # except StaleElementReferenceException:
        #     print(
        #         "Stale element reference. The page structure might have changed or the element might have been removed.")
