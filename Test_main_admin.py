import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class PHPTravelsLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        chrome_driver = "driver\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://www.phptravels.net/admin")

        # Wait until Page fully loads and Flight Tab gets available
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located( (By.ID, "layoutAuthentication_content"))
        )
        # Navigate to Flight Tab
        element.click()
        time.sleep(2)

    def test_valid_login(self):
        driver = self.driver
        #driver.get("http://www.phptravels.net/admin")
        elem = driver.find_element(By.NAME,"email")
        elem.send_keys("admin@phptravels.com")
        elem = driver.find_element(By.NAME,"password")
        elem.send_keys("demoadmin")
        elem.send_keys(Keys.RETURN)
        # Make sure you wait for the page to load completely
        time.sleep(3)
        assert "Quick Booking" in driver.page_source

    def test_invalid_login(self):
        driver = self.driver
        
        elem = driver.find_element(By.NAME,"email")
        elem.send_keys("invalid@invalid.com")
        elem = driver.find_element(By.NAME,"password")
        elem.send_keys("invalid")
        elem.send_keys(Keys.RETURN)
        # Make sure you wait for the page to load completely
        time.sleep(3)
        assert "Invalid Login Credentials" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()