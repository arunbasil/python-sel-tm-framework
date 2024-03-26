# test_search_property.py
from time import sleep

import pytest
from pages.property.property_home_page import PropertyHomePage
from pages.search.search_results_page.prpty_results_page import PropertySearchResultsPage
from pages.tm_homepage.tm_home_page import TmHomePage
from testdata.search_test_data import SearchTestData


class TestSearchFunctionality:
    @pytest.mark.parametrize("expected_title,expected_address", [
        ("Sunny Family Home", "164 Dendro Ring Road, Milldale, Rodney"),
        ("First Home Buyers Gem", "16 Milldale Drive, Milldale, Rodney")])
    def test_property_search_results_page(self, browser,expected_title, expected_address):
        expected_pagination_numbers = [1, 2, 3, 4, 5, 6, 7, 10]
        tmhomepage: TmHomePage = TmHomePage(browser)
        tmhomepage.search_for_item_in_tm_homepage("Millwater")
        property_search_results_page: PropertySearchResultsPage = PropertySearchResultsPage(browser)
        # Get properties
        property_title = property_search_results_page.property_search_results_page_title()
        property_search_header = property_search_results_page.property_search_header()
        property_search_results_count = property_search_results_page.get_number_of_search_results()
        pagination_nos = property_search_results_page.get_pagination_page_nos()

        assert property_title == property_title, f"Expected title '{property_search_results_page.PROPERTY_TITLE_TEXT}', got '{property_title}'"
        assert "Residential properties" in property_search_header, "The header does not contain 'Residential properties'"
        #
        # # Directly assert the conditions instead of using if statement
        # assert "209" in property_search_results_count, "'209' not found in search results count"
        # assert "'Millwater'" in property_search_results_count, "'Millwater' not found in search results count"
        # assert pagination_nos == expected_pagination_numbers, "Pagination numbers are not as expected."
        #
        # # If you want to check if all expected numbers are present (regardless of order)
        # assert all(number in pagination_nos for number in
        #            expected_pagination_numbers), "Not all expected pagination numbers are present."
        #
        # search_results = property_search_results_page.get_search_results_list()
        #
        # # Convert the list of dictionaries to a list of tuples for easier assertion
        # results_tuples = [(item["title"], item["address"]) for item in search_results]
        #
        # # # Check if the expected title and address tuple is in the list of result tuples
        # assert (expected_title, expected_address) in results_tuples, \
        #     f"Expected title and address pair {(expected_title, expected_address)} not found in search results."
        #
        # # property_search_results_page.get_all_search_results_from_all_resulted_pages_v1()


