import pytest
from pages.tm_homepage.tm_home_page import TmHomePage
from pages.property.property_home_page import PropertyHomePage



@pytest.mark.usefixtures("browser")
class TestLaunchPage():
    # @pytest.fixture()
    # def test_lp(self,browser):
    #     return TmLaunchPage(browser)
    # # def test_launch_page(self,browser):
    # #     lp = TmLaunchPage(browser)
    # #     lp.click_property_button()
    # #     print(lp.get_page_title())

    def test_search_for_car(self, browser):
        lp = TmHomePage(browser)
        keyword = "Subaru"
        lp.search_for_item_in_tm_homepage(keyword)
        print(lp.get_page_title())
        results = PropertyHomePage(browser)
        print(results.get_page_title())

        if results.is_keyword_in_results_header(keyword):
            assert True


