from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

# Initialize and return a Chrome WebDriver with specified options.
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-position=-2000,0")  # Hides the window
    return webdriver.Chrome(options=chrome_options)

# Handles the dropdown selection and returns the selected option's text.
def select_dropdown_option(driver, element_id, context_message):
    dropdown = Select(driver.find_element(By.ID, element_id))
    print(context_message)
    for index, option in enumerate(dropdown.options[1:], start=1):
        print(f"{index}. {option.text.strip()}")
    selected_index = int(input("\nChoose an option by entering the corresponding number: "))

    # Ensure that the selected index is within the valid range
    if selected_index < 1 or selected_index >= len(dropdown.options):
        print("\nInvalid option selected. Please try again.")
        return None

    dropdown.select_by_index(selected_index)
    print("\nSelected option:", dropdown.first_selected_option.text)
    return dropdown.first_selected_option.text

def get_survey_numbers():
    # Navigates through dropdowns on a website to display survey numbers.
    driver = init_driver()
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")
    time.sleep(5)  # Allow page elements to load

    try:
        # Select district using the generalized function
        selected_district = select_dropdown_option(driver, "districtID", "\nAvailable district names are:")
        if not selected_district:
            return
        time.sleep(5)

        # Select district using the generalized function
        selected_mandal = select_dropdown_option(driver, "mandalID", f"\nAvailable Mandal names in {selected_district} district are:")
        if not selected_mandal:
            return
        time.sleep(5)

        # Select village using the generalized function
        selected_village = select_dropdown_option(driver, "villageId", f"\nAvailable Village names in {selected_district} district and {selected_mandal} mandal are:")
        if not selected_village:
            return
        time.sleep(5)

        # Display survey numbers
        surveyId_dropdown = Select(driver.find_element(By.ID, "surveyIdselect"))
        print(f"\nThe {selected_village}  Village of {selected_mandal}  Mandal in {selected_district}  District has total {len(surveyId_dropdown.options[1:])} survey numbers :")
        for index, option in enumerate(surveyId_dropdown.options[1:], start=1):
            print(f"{index}. Survey # {option.text.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Test the function
get_survey_numbers()
