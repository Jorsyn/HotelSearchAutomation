from selenium.webdriver.common.by import By

# Assign locators
# page 1
accept_button_id = "didomi-notice-agree-button"
search_input_id = "mbe-destination-input"
dates_selector = "//div[@id='mbe-dates-select']"
xpath_available_dates = "//div[@class='mbe-calendar']//li[contains(@class,'available')]"
rooms_input_id = "mbe-rooms-input"
accept_rooms_xpath = "//div[@class='mbe-room-btn']/button[@class='mbe-btn']"
final_search_button_id = "mbe-search-button"

# page 2
rooms_locator = "//div[@class='c-hotel-sheet-room__content-content']"