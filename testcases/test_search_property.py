import pytest
from pages.search.search_results_page.prpty_results_page import PropertySearchResultsPage
from pages.tm_homepage.tm_home_page import TmHomePage

# Define a mapping for search term to page object
PAGE_TYPE_MAPPING = {
    'Millwater': PropertySearchResultsPage
    # 'Subaru': AutoSearchResultsPage

}
@pytest.fixture
def dynamic_search_results_page(browser, search_term):
    tm_home_page = TmHomePage(browser)
    tm_home_page.search_for_item_in_tm_homepage(search_term)
    page_class = PAGE_TYPE_MAPPING.get(search_term)
    if not page_class:
        raise ValueError(f"No result page defined for search term '{search_term}'")
    return page_class(browser)


@pytest.mark.parametrize("search_term, expected_title, expected_address, expected_page_type", [
    ("Millwater", "Welcome to your Dream Maddren Home", "5 Kereru Lane, Millwater, Rodney", PropertySearchResultsPage),
    # ("Subaru", "Subaru Legacy 2010", "123 Car Street, CarCity", AutoSearchResultsPage),
    # Add more test cases as needed
])
def test_dynamic_search_results_contains_expected_data(browser, dynamic_search_results_page, search_term,
                                                       expected_title, expected_address, expected_page_type):
    assert isinstance(dynamic_search_results_page, expected_page_type), \
        f"Expected page type does not match for search term '{search_term}'"

    # Direct assertions without local variables unless they add clarity
    assert "Residential properties" in dynamic_search_results_page.property_search_header(), \
        "The header does not contain 'Residential properties'"

    # Get all search results from all pages
    search_results = dynamic_search_results_page.collect_search_results_from_all_pages()

    # Convert to list of tuples
    results_tuples = [(item["title"], item["address"]) for item in search_results]

    # Assert expected data is in the search results
    assert (expected_title, expected_address) in results_tuples, \
        f"Expected title and address pair {(expected_title, expected_address)} not found in search results."





# # test_search_property.py
# from time import sleep
#
# import pytest
# from pages.property.property_home_page import PropertyHomePage
# from pages.search.search_results_page.prpty_results_page import PropertySearchResultsPage
# from pages.tm_homepage.tm_home_page import TmHomePage
# from testdata.search_test_data import SearchTestData
#
#
# class TestSearchFunctionality:
#     # @pytest.mark.parametrize("expected_title,expected_address", [
#     #     ("Welcome to your Dream Maddren Home", "5 Kereru Lane, Millwater, Rodney"),
#     #     ("Charming New Family Home in Milldale", "291 Te Taruna Drive, Milldale, Rodney")])
#     # def test_property_search_results_page(self, browser, expected_title, expected_address):
#     def test_property_search_results_page(self, browser):
#         expected_pagination_numbers = [1, 2, 3, 4, 5, 6, 7, 10]
#         tmhomepage: TmHomePage = TmHomePage(browser)
#         tmhomepage.search_for_item_in_tm_homepage("Millwater")
#         property_search_rlts_page: PropertySearchResultsPage = PropertySearchResultsPage(browser)
#         # Get properties
#         property_title = property_search_rlts_page.property_search_results_page_title()
#         property_search_header = property_search_rlts_page.property_search_header()
#         property_search_results_count = property_search_rlts_page.get_number_of_search_results()
#         pagination_nos = property_search_rlts_page.get_pagination_page_nos()
#
#         # Assertions with messages
#         # assert property_title == property_title, f"Expected title '{property_search_rlts_page.PROPERTY_TITLE_TEXT}', got '{property_title}'"
#         # assert "Residential properties" in property_search_header, "The header does not contain 'Residential properties'"
#         search_results = property_search_rlts_page.collect_search_results_from_all_pages()
#
#         sleep(4)
#
#         # # Directly assert the conditions instead of using if statement
#         # assert "209" in property_search_results_count, "'209' not found in search results count"
#         # assert "'Millwater'" in property_search_results_count, "'Millwater' not found in search results count"
#         # assert pagination_nos == expected_pagination_numbers, "Pagination numbers are not as expected."
#         #
#         # # If you want to check if all expected numbers are present (regardless of order)
#         # assert all(number in pagination_nos for number in
#         #            expected_pagination_numbers), "Not all expected pagination numbers are present."
#         #
#         # search_results = property_search_rlts_page.get_search_results_list()
#         #
#         # # Convert the list of dictionaries to a list of tuples for easier assertion
#         # results_tuples = [(item["title"], item["address"]) for item in search_results]
#         #
#         # # # Check if the expected title and address tuple is in the list of result tuples
#         # assert (expected_title, expected_address) in results_tuples, \
#         #     f"Expected title and address pair {(expected_title, expected_address)} not found in search results."
#         #
#         # # property_search_rlts_page.get_all_search_results_from_all_resulted_pages_v1()
#         # assert property_title == property_title, f"Expected title '{property_search_rlts_page.PROPERTY_TITLE_TEXT}', got '{property_title}'"
#         # assert "Residential properties" in property_search_header, "The header does not contain 'Residential properties'"
#         #
