from selenium.webdriver.common.by import By


# Locator for Home page
class HomePageLocators:
    """A class for main page locators. All main page locators should come here"""
    FLIGHT_TAB = (By.ID, 'flights-tab')  #data-bs-target="#flights"     //a[@href='#flights']"
    FORM_NAME = (By.NAME, 'flightmanualSearch')
    FROM = (By.ID, 's2id_location_from')
    TO = (By.ID, 's2id_location_to')
    DEPART = (By.ID, 'FlightsDateStart')
    ADULTS = (By.NAME, 'fadults')
    CHILD = (By.NAME, 'fchildren')
    INFANT = (By.NAME, 'finfant')
    ADULTS_MINUS_BTN = (By.XPATH, "(//button[text()='-'])[3]")
    ADULTS_PLUS_BTN = (By.XPATH, "(//button[text()='+'])[3]")
    ROUND_TRIP = (By.XPATH, "//label[@for='flightSearchRadio-1']")
    RETURN_DATE = (By.ID, "FlightsDateEnd")


class SearchResultPageLocators:
    MODIFY_SEARCH = (By.XPATH, "//button[contains(@class,'btn btn-secondary')]")
    CHANGE_SEARCH = (By.ID, "change-search")
    FLIGHT_INFO = (By.XPATH, "//div[@data-toggle='collapse']")
    FLIGHT_ADDITIONAL_INFO = (By.ID, "searchResultsItem-0")
    LANG_DROPDOWN = (By.ID, "dropdownCurrency")
    INR_SELECTION = (By.XPATH, "//a[@data-code='18']")
    CURRENCY_TYPE_FLIGHT = (By.XPATH, "//p[@class='theme-search-results-item-price-tag']//strong")
