from selenium.webdriver.common.by import By
# from utilities.selenium_utils import Utils
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_driver import BaseDriver
from selenium.webdriver.remote.webelement import WebElement


class TmVerticalSearch(BaseDriver):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    # ELEMENTS THAT CAN BE CLICKED

    PROPERTY_BUTTON = (By.XPATH,
                       "/html/body/tm-root/div[1]/main/div/tm-dynamic-homepage/tm-homepage-in-with-the-new-campaign-header/nav/div[2]/tm-homepage-search-header-vertical-list/ul/li[4]/a")

    #     ACTIONS
    def click_property_button(self):
        self.driver.find_element(self.PROPERTY_BUTTON)
