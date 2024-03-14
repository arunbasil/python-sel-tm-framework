from selenium.webdriver.common.by import By
# from utilities.selenium_utils import Utils
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_driver import BaseDriver
from selenium.webdriver.remote.webelement import WebElement

class TmLaunchPage(BaseDriver):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
    
    SEARCH_TEXT_BOX = (By.XPATH,'//*[@id="search"]')
    SEARCH_BUTTON = (By.XPATH,"//button[@aria-label='Search all of Trade Me']")
    PROPERTY_BUTTON = (By.XPATH,"//a[@class='tm-homepage-search-header__vertical-links-link tm-homepage-search-header__vertical-links-link--property']")
    EXPECTED_TITLE = "Search New Zealand's largest range of houses and properties for sale - Trade Me | Trade Me Property"
# SEARCH FUNCTIONS:
    def get_search_text_box(self) -> WebElement:
        return self.driver.find_element(*self.SEARCH_TEXT_BOX)
    
    def enter_search_text(self, text: str):
        self.enter_text(self.get_search_text_box(),text)

    def click_search_button(self):
        print(f"{type(self.driver)} = {self.driver} and {type(self.SEARCH_BUTTON)} = {self.SEARCH_BUTTON}")
        self.wait_for_element_clickable(self.SEARCH_BUTTON).click()
        # search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        # search_button.click()

    def search_for_item(self, item_name: str):
        self.enter_search_text(item_name)
        self.click_search_button()

    # def click_property_button(self):
    #     # self.driver.find_element(*self.PROPERTY_BUTTON).click()
    #     Utils.wait_for_element(self.driver,self.PROPERTY_BUTTON,10).click()
    #     Utils.wait_for_page_load(self.driver,self.EXPECTED_TITLE,10)

    # def get_page_title(self) -> str:
    #     return self.driver.title
        