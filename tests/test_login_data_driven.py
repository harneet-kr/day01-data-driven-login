"""Data-driven login tests
Tests login with multiple users from CSV file"""

import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Read test data from csv
def get_test_data():
    """Read user data from CSV file"""
    test_data = []
    with open('test_data/users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test_data.append((row['username'], row['password'], row['expected_result']))
    return test_data

class TestLoginDataDriven:
    """Data-driver Login tests"""

    def setup_method(self):
        """Setup browser before each test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        time.sleep(1)

    def teardown_method(self):
            """Close browser after each test"""
            time.sleep(1)
            self.driver.quit()

    @pytest.mark.parametrize("username, password, expected_result", get_test_data())
    def test_login_multiple_user(self, username, password, expected_result):
            """Test login with different user from CSV"""

            #Enter Credentials
            self.driver.find_element(By.ID, "user-name").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "login-button").click()
            time.sleep(2)

            #verify based on expected result
            if expected_result == "pass":
                #Should be on products page
                assert "inventory.html" in self.driver.current_url
                print(f" {username}: Login successful")

            elif expected_result == "locked":
                #Should see locked out error
                error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
                assert "locked out" in error.text.lower()
                print(f"{username}: Locked error shown correctly")

            elif expected_result == "fail":
                #Should see error message
                error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
                assert error.is_displayed()
                print(f"{username}: Invalid login rejected correctly")