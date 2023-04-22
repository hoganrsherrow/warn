from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def scrape_table(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    headers = [header.text for header in table.find_all("th")]
    rows = table.find_all("tr")[1:]  # Skip the header row

    data = []
    for row in rows:
        tds = [td.text.strip() for td in row.find_all("td")]
        data.append(dict(zip(headers, tds)))

    return data

def scrape_web_de(url="https://joblink.delaware.gov/search/warn_lookups/new"):
    print("Grabbing DE web results...")
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get(url)

    # Wait for the button with the class 'button' to be present
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.presence_of_element_located((By.ID, 'input11')))

    # Click the button
    button.click()

    # Set first page
    page_number = 1

    # Data to be returned
    data = []

    # scrape the table
    while True:
        time.sleep(2)
        data.extend(scrape_table(driver))
        page_number += 1

        # Find next page of the table if there is one
        try:
            next_page_link = driver.find_element("xpath", f"/html/body/div[1]/main/section/nav/div/div/a[contains(text(), '{page_number}')]")
        except NoSuchElementException:
            print(f"page link {page_number} not found")
            break
        
        if next_page_link:
            print(f"page number {page_number} clicked")
            next_page_link.click()

    # Quit the driver
    driver.quit()

    # Return data list
    return data
