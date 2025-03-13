import time
import selenium
import pandas
import matplotlib
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://www.expedia.com/")

try:
    # ✅ Click the Flights Tab
    flights_tab = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Flights')]"))
    )
    flights_tab.click()
    print("✅ Clicked Flights tab")

    # ✅ Ensure we are in the Round Trip section
    round_trip_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-controls, 'FlightSearchForm_ROUND_TRIP')]"))
    )
    round_trip_tab.click()
    print("✅ Selected Round Trip option")

 # ✅ Select Business Class (Change to 'Economy' or 'First Class' if needed)
    class_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cabin_class']/span"))
    )
    class_dropdown.click()
    print("✅ Opened Travel Class Dropdown")

    # ✅ Select Business Class from the dropdown
    class_selection = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Business class')]"))
    )
    class_selection.click()
    print("✅ Selected Business Class")

    # ✅ Scroll to and Click the "Leaving from" button AFTER selecting class
    departure_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']//button[contains(@aria-label, 'Leaving from')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", departure_button)
    departure_button.click()
    print("✅ Clicked 'Leaving from' button")

    # ✅ Enter Departure City
    departure_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']//input[contains(@aria-label, 'Leaving from')]"))
    )
    departure_input.click()
    departure_input.send_keys("New York")
    print("✅ Entered Departure City")

except Exception as e:
    print("❌ Error:", e)

driver.quit()



