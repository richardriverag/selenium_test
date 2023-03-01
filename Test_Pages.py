import time

from Test_locators import HomePageLocators, SearchResultPageLocators

import datetime


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    
    # To fill the information which doesn't have default value
    def fill_non_default_fields(self):
        tomorrows_date = str(datetime.date.today() + datetime.timedelta(days=1))
        # Form has default value for all other fields except depart date, so entering that
        self.driver.execute_script(
            "document.getElementById('" + HomePageLocators.DEPART[1] + "').value = '" + tomorrows_date + "'")

    # Click on Flight Search Button
    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*HomePageLocators.FORM_NAME)
        element.submit()

    # Return status whether flight list found or not
    def is_flights_available(self):
        return 'Flights List' in self.driver.title

    def click_negative_btn(self):
        self.driver.find_element(*HomePageLocators.ADULTS_MINUS_BTN).click()
        return int(self.driver.find_element(*HomePageLocators.ADULTS).get_attribute('value'))

    def click_positive_btn(self):
        self.driver.find_element(*HomePageLocators.ADULTS_PLUS_BTN).click()
        return int(self.driver.find_element(*HomePageLocators.ADULTS).get_attribute('value'))


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "Search Results" not in self.driver.title

    def is_slide_visible(self):
        """
        Check Whether additional info popup window slides down or not
        :return: True if displayed else False
        """
        self.driver.find_element(*SearchResultPageLocators.FLIGHT_INFO).click()
        time.sleep(2)
        return self.driver.find_element(*SearchResultPageLocators.FLIGHT_ADDITIONAL_INFO).is_displayed()
