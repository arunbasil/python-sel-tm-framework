import pytest
from pages.search.search_results_page.prpty_results_page import PropertySearchResultsPage
from pages.tm_homepage.tm_home_page import TmHomePage
from utilities.screenshot_util import take_screenshot

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
    take_screenshot(browser, 'test_my_feature')

    # Convert to list of tuples
    results_tuples = [(item["title"], item["address"]) for item in search_results]

    # Assert expected data is in the search results
    assert (expected_title, expected_address) in results_tuples, \
        f"Expected title and address pair {(expected_title, expected_address)} not found in search results."



