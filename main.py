import unittest
from selenium import webdriver
import Pages

page1 = "https://www.melia.com/es/home.htm"
page2 = "https://www.melia.com/es/hoteles/espana/madrid/melia-castilla/habitaciones.htm"
print("Note: This script requires selenium and google chrome with a version matching a GC webdriver located in PATH to work")
print("Google chrome webdriver version 100 it attached to this project")

class Tests(unittest.TestCase):
    def setUp(self):
        # Opening the browser
        # This will be the path if you clone the github repository to the default location: home
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        # browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        # Closing the browser
        self.driver.quit()

    def test_1_search_random_location_and_dates(self):
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


if __name__ == '__main__':
    unittest.main()