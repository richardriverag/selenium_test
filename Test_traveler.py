import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class PHPHTravelerLogin(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        chrome_driver = "driver\chromedriver.exe" 
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.maximize_window()
    
    def setUp(self):
        self.driver.get("https://www.phptravels.net/admin")
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, "email" ))
        )
        time.sleep(2)
    
    def test_valid_login(self):
        driver = self.driver
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("admin@phptravels.com")
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys("demoadmin")
        elem.send_keys(Keys.RETURN)
        #make sure you wait for the page load completely
        time.sleep(3)
        assert "Redirecting" in driver.page_source
    
    def test_invalid_login(self):
        driver = self.driver
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("invalid@phptravels.com")
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys("invalid")
        elem.send_keys(Keys.RETURN)
        #make sure you wait for the page load completely
        time.sleep(5)
        assert "Invalid Login Credentials" in driver.page_source
    
    def tearDown(self):
        self.driver.close()
        
        





if __name__ == "__main__":
    unittest.main()
    