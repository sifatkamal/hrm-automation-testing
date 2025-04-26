import os
import hrm.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

class HRM:

    def __init__(self, driver_path = r"C:/SeleniumDrivers", teardown = False):

        self.driver_path = driver_path
        self.teardown = teardown

        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if self.teardown == True:
            
            self.driver.quit()

    def login_page(self):

        self.driver.get(const.LOGIN_URL)

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys("Admin")

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("admin123")

        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def applyLeave(self):

        time.sleep(4)

        self.driver.get(const.APPLY_LEAVE)

        try:

            error = self.driver.find_element(By.CSS_SELECTOR, 'p[class="oxd-text oxd-text--p oxd-text--subtitle-2"]').text

            if error == "No Leave Types with Leave Balance":

                self.driver.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab.--parent:nth-of-type(1)").click()

                self.driver.find_element(By.XPATH, '(//span[@class="oxd-topbar-body-nav-tab-item"]) [1]').click()

                self.driver.find_element(By.XPATH, '(//a[@class="oxd-topbar-body-nav-tab-link"])[1]').click()

                user_name = self.driver.find_element(By.CSS_SELECTOR, 'p[class="oxd-userdropdown-name"]').text

                self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]').send_keys(user_name)

                time.sleep(3)

                self.driver.find_element(By.CSS_SELECTOR, 'div[role="listbox"]').click()

                time.sleep(5)

                self.driver.find_element(By.XPATH, '(//div[@class="oxd-select-text-input"])[1]').click()

                options = self.driver.find_elements(By.XPATH, '//div[@role="listbox"]/*')

                for i in options:

                    if i.text == "CAN - FMLA":

                        i.click()

                        break

                self.driver.find_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]').send_keys(3)

                self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

                self.driver.find_element(By.XPATH, '(//button[@type="button"])[6]').click()

                time.sleep(2)

                self.driver.get(const.APPLY_LEAVE)                

        except:

            pass

        self.driver.find_element(By.CSS_SELECTOR, 'div[class="oxd-select-text oxd-select-text--active"]').click()

        options = self.driver.find_elements(By.XPATH, '//div[@role="listbox"]/*')

        for i in options:

            if i.text == "CAN - FMLA":

                i.click()

                break

        self.driver.find_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]').send_keys("2024-12-12")

        self.driver.find_element(By.XPATH, '(//textarea[@class="oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical"])').send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry")

        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()







