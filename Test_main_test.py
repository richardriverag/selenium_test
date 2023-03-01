import time
import unittest
import Test_Pages as Page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Test_locators import HomePageLocators, SearchResultPageLocators


class FlightSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        chrome_driver = "driver\chromedriver.exe"
        cls.driver = webdriver.Chrome(chrome_driver)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://www.phptravels.net")

        # Wait until Page fully loads and Flight Tab gets available
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(HomePageLocators.FLIGHT_TAB)
        )
        # Navigate to Flight Tab
        element.click()
        time.sleep(2)

    # TC 1
    def test_flight_search(self):
        main_page = Page.MainPage(self.driver)
        main_page.fill_non_default_fields()
        main_page.click_search_button()

        # Verifies that the Flight list is displayed
        assert main_page.is_flights_available(), True
    """
    # TC 2
    def test_adult_negative_count(self):
        main_page = Page.MainPage(self.driver)
        adults_count = main_page.click_negative_btn()

        # Added time to avoid infinite loop (will exit after 1min when conditions are not met)
        t_end = time.time() + 60
        while (adults_count != 0) and (time.time() < t_end):
            adults_count = main_page.click_negative_btn()

        adults_count = main_page.click_negative_btn()
        self.assertEqual(adults_count < 0, False)

    # TC 3
    def test_adult_positive_count(self):
        main_page = Page.MainPage(self.driver)
        adults_count = main_page.click_positive_btn()

        # Added time to avoid infinite loop (will exit after 1min when conditions are not met)
        t_end = time.time() + 60
        while (adults_count != 100) and (time.time() < t_end):
            adults_count = main_page.click_positive_btn()

        adults_count = main_page.click_positive_btn()
        self.assertEqual(adults_count == 101, False)

    # TC 4
    def test_round_trip(self):

        # Check that 'RETURN' field is not displayed for ONE WAY journey type
        is_displayed = self.driver.find_element(*HomePageLocators.RETURN_DATE).is_displayed()
        self.assertEqual(is_displayed, False)

        # Select journey type as ROUND TRIP
        self.driver.find_element(*HomePageLocators.ROUND_TRIP).click()
        time.sleep(2)

        # Check that 'RETURN' field is displayed for ROUND TRIP journey type
        is_displayed = self.driver.find_element(*HomePageLocators.RETURN_DATE).is_displayed()

        self.assertEqual(is_displayed, True)

    # TC 5
    def test_modify_search(self):

        main_page = Page.MainPage(self.driver)
        main_page.fill_non_default_fields()
        main_page.click_search_button()

        # Check that Change Search field is not displayed before clicking on 'MODIFY SEARCH' Button
        is_displayed = self.driver.find_element(*SearchResultPageLocators.CHANGE_SEARCH).is_displayed()

        self.assertEqual(is_displayed, False)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(SearchResultPageLocators.MODIFY_SEARCH)
        ).click()
        time.sleep(2)

        # Check that Change Search field is displayed
        is_displayed = self.driver.find_element(*SearchResultPageLocators.CHANGE_SEARCH).is_displayed()

        self.assertEqual(is_displayed, True)

    # TC 7
    def test_trip_info_slider(self):
        main_page = Page.MainPage(self.driver)
        main_page.fill_non_default_fields()
        main_page.click_search_button()

        resulting_page = Page.SearchResultsPage(self.driver)
        result = resulting_page.is_slide_visible()

        self.assertEqual(result, True)
    
    def test_check_currency(self):
        main_page = Page.MainPage(self.driver)
        main_page.fill_non_default_fields()
        main_page.click_search_button()
        self.driver.find_element(*SearchResultPageLocators.LANG_DROPDOWN).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(SearchResultPageLocators.INR_SELECTION)
        ).click()
        time.sleep(5)

        amount = self.driver.find_element(*SearchResultPageLocators.CURRENCY_TYPE_FLIGHT).text

        assert (True if 'INR' in amount else False), True
    """
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
