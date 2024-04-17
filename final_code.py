from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def get_survey_numbers():
    try:
        # Initialize Chrome WebDriver
        driver = webdriver.Chrome()
        driver.get("https://dharani.telangana.gov.in/knowLandStatus")
        # Minimize the browser window
        driver.minimize_window()

        # Prompt the user to enter their district choice
        print("\nPlease choose your district:")
        district_dropdown = Select(driver.find_element(By.ID, "districtID"))
        for index, option in enumerate(district_dropdown.options[1:], start=1):
            print(f"{index}. {option.text.strip()}")
        selected_index = int(input("\nEnter the number corresponding to your district choice: "))
        if selected_index < 1 or selected_index >= len(district_dropdown.options):
            print("Invalid option selected for district. Please try again.")
            return
        district_dropdown.select_by_index(selected_index)

        # Get the selected district
        selected_district = district_dropdown.first_selected_option.text
        print("\nSelected District:", selected_district)
        time.sleep(2)

        # Prompt the user to enter their mandal choice
        print(f"\nPlease choose your Mandal in {selected_district}:")
        mandal_dropdown = Select(driver.find_element(By.ID, "mandalID"))
        for index, option in enumerate(mandal_dropdown.options[1:], start=1):
            print(f"{index}. {option.text.strip()}")
        selected_index = int(input("\nEnter the number corresponding to your mandal choice: "))
        if selected_index < 1 or selected_index >= len(mandal_dropdown.options):
            print("Invalid option selected for mandal. Please try again.")
            return
        mandal_dropdown.select_by_index(selected_index)
        selected_mandal = mandal_dropdown.first_selected_option.text
        print("Selected Mandal :", selected_mandal)
        time.sleep(2)

        # Prompt the user to enter their village choice
        print(f"\nPlease choose your Village in {selected_mandal}  Mandal of {selected_district}  District:")
        village_dropdown = Select(driver.find_element(By.ID, "villageId"))
        for index, option in enumerate(village_dropdown.options[1:], start=1):
            print(f"{index}. {option.text.strip()}")
        selected_index = int(input("\nEnter the number corresponding to your village choice: "))
        if selected_index < 1 or selected_index >= len(village_dropdown.options):
            print("Invalid option selected for village. Please try again.")
            return
        village_dropdown.select_by_index(selected_index)
        selected_village = village_dropdown.first_selected_option.text
        print("Selected Village :", selected_village)
        time.sleep(2)

        # Display the available survey numbers for the selected village
        surveyId_dropdown = Select(driver.find_element(By.ID, "surveyIdselect"))
        print(f"\nThe {selected_village}  Village of {selected_mandal}  Mandal in {selected_district}  District has total {len(surveyId_dropdown.options[1:])} survey numbers :")
        for index, option in enumerate(surveyId_dropdown.options[1:], start=1):
            print(f"{index}. Survey Number: {option.text.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver session
        driver.quit()

# Test the function
get_survey_numbers()
