import requests
import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from io import BytesIO

def scrape_web_tx(url="https://www.twc.texas.gov/businesses/worker-adjustment-and-retraining-notification-warn-notices"):
    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Find all the links on the page
    links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '.xlsx')]")))

    # Download all .xlsx files
    for link in links:
        response = requests.get(link.get_attribute('href'))

        workbook = openpyxl.load_workbook(BytesIO(response.content))
        sheet = workbook.active
        col_headers = [cell.value for cell in sheet[1]]

        print(f"Contents of {link}:")
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_str = ""
            for header, value in zip(col_headers, row):
                row_str += f"{header}: {value}, "
            print(row_str)
        print()


    # Close the browser
    driver.quit()