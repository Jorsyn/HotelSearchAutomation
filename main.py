import unittest
from selenium import webdriver
import Pages

page1 = "https://www.melia.com/es/home.htm"
page2 = "https://www.melia.com/es/hoteles/espana/madrid/melia-castilla/habitaciones.htm"


class Tests(unittest.TestCase):
    def setUp(self):
        # Opening the browser
        self.driver = webdriver.Chrome()
        # browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        # Closing the browser
        self.driver.quit()

    def test_1_search_random_location_and_dates_Melia(self):
        print('\nStarting task 1')
        self.page = Pages.SearchPage(self.driver)
        self.page.navigate_to(page1)
        self.page.accept_popup()
        self.page.search_for_destination("Madrid")
        self.page.chose_first_two_available_dates()
        self.page.accept_rooms()
        self.page.get_search_results()
        print('End of task 1')

    def test_2_list_all_rooms_on_page(self):
        print('\nStarting task 2')
        self.page = Pages.ListingsPage(self.driver)
        self.page.navigate_to(page2)
        self.page.accept_popup()
        self.page.list_number_of_rooms()
        print('Task 2 finished successfully')


