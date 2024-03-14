
from os import wait
import pytest
from pages.tm_homepage.tm_home_page import TmLaunchPage


@pytest.mark.usefixtures("browser") 
class TestLauchPage():
    # @pytest.fixture()
    # def test_lp(self,browser):
    #     return TmLaunchPage(browser)
    # # def test_launch_page(self,browser):
    # #     lp = TmLaunchPage(browser)
    # #     lp.click_property_button()
    # #     print(lp.get_page_title())
        
    
    def test_search_for_car(self,browser):
        lp = TmLaunchPage(browser)
        lp.search_for_item("Subaru")
        print(browser.get_page_title)
