import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class CreateActivityPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--ignore-certificate-errors")  # <-- key line
        options.add_argument("--allow-insecure-localhost")  # optional, but useful
        options.add_argument("--headless")  # for CI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        cls.driver.implicitly_wait(10)
        cls.base_url = "https://localhost"

        # Use the seeded email and password created to test create activity
        cls.seeded_email = "2301875@sit.singaporetech.edu.sg"
        cls.seeded_password = "123123123"

    def fill_login_form(self, email, password):
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "login-btn").click()
        time.sleep(2)

    def fill_activity_form(self, name, date):
        # Fill in the activity form
        self.driver.find_element(By.ID, "activityNameInput").send_keys(
            "Selenium Test Activity"
        )
        self.driver.find_element(By.ID, "activityTypeInput").send_keys("Sports")
        self.driver.find_element(By.ID, "skillsReqInput").send_keys("None")

        date_input = self.driver.find_element(By.ID, "dateInput")
        self.driver.execute_script(
            "arguments[0].value = arguments[1]", date_input, date
        )

        self.driver.find_element(By.ID, "locationInput").send_keys("Test Field")
        self.driver.find_element(By.ID, "maxPaxInput").clear()
        self.driver.find_element(By.ID, "maxPaxInput").send_keys("10")

        # Submit the form
        modal = self.driver.find_element(By.ID, "hostModal")
        modal.find_element(By.XPATH, ".//button[contains(text(), 'Host')]").click()
        time.sleep(2)

    def test_create_activity_success(self):
        try:
            # Assert that the login with the seeded email and password is successful
            # After login, the user should be redirected to the bulletin board page
            self.fill_login_form(email=self.seeded_email, password=self.seeded_password)
            self.assertIn("Bulletin Board", self.driver.page_source)

            # Open the host activity modal
            host_button = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Host Activity')]"
            )
            host_button.click()
            time.sleep(1)  # Wait for modal animation

            self.fill_activity_form(
                name="Selenium Test Activity", date="3000-07-08T15:30"
            )

            # Assert that the activity was created successfully
            self.assertIn("Selenium Test Activity", self.driver.page_source)

            # Logout to reset the state for the next test
            self.driver.get(f"{self.base_url}/logout")

        except Exception as e:
            os.makedirs("artifacts", exist_ok=True)
            self.driver.save_screenshot("artifacts/create_activity_success.png")
            with open("artifacts/debug.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise  # Re-raise so the test still fails

    def test_create_activity_past_date(self):
        try:
            # Assert that the login with the seeded email and password is successful
            # After login, the user should be redirected to the bulletin board page
            self.fill_login_form(email=self.seeded_email, password=self.seeded_password)
            self.assertIn("Bulletin Board", self.driver.page_source)

            # Open the host activity modal
            host_button = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Host Activity')]"
            )
            host_button.click()
            time.sleep(1)  # Wait for modal animation

            self.fill_activity_form(
                name="Past Date Activity",
                date="2000-07-08T15:30",  # Past date for testing failure
            )

            wait = WebDriverWait(self.driver, 10)
            error_elem = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#flashModal .flash-message.error")
                )
            )
            self.assertIn("Date cannot be in the past", error_elem.text)

            # Logout to reset the state for the next test
            self.driver.get(f"{self.base_url}/logout")

        except Exception as e:
            os.makedirs("artifacts", exist_ok=True)
            self.driver.save_screenshot("artifacts/create_activity_success.png")
            with open("artifacts/debug.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise  # Re-raise so the test still fails

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
