import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


class BasePage():
    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def navigate_to(self, page):
        self.driver.get(page)

    def accept_popup(self):
        self.driver.find_element(By.ID, Locators.accept_button_id).click()

class SearchPage(BasePage):

    def search_for_destination(self, text):
        # find and open search input
        search_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, Locators.search_input_id)))
        # search_input.click()
        self.driver.execute_script("arguments[0].click();", search_input)

        # type in destination
        search_input.send_keys(text)
        # Select first result
        search_input.send_keys(Keys.ARROW_DOWN)
        search_input.send_keys(Keys.ENTER)


    def chose_first_two_available_dates(self):
        dates_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, Locators.dates_selector)))
        dates_input.click()
        time.sleep(2)
        available_dates = self.driver.find_elements(By.XPATH, Locators.xpath_available_dates)
        available_dates[0].click()
        available_dates[1].click()

    def accept_rooms(self):
        # this is strictly not necessary, as the room info is accepted by default
        self.driver.find_element(By.ID, Locators.rooms_input_id).click()
        self.driver.find_element(By.XPATH, Locators.accept_rooms_xpath).click()

    def get_search_results(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, Locators.final_search_button_id))).click()


class ListingsPage(BasePage):
    def list_number_of_rooms(self):
        rooms = self.driver.find_elements(By.XPATH, Locators.rooms_locator)
        print("Number of rooms found on page:", len(rooms))
