from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def scrape_web_fl(url="https://reactwarn.floridajobs.org/WarnList/Records?year=2023"):
    print("Grabbing FL web results...")
    driver = webdriver.Chrome() # new web driver
    driver.get(url)

    wait = WebDriverWait(driver, 10) # wait until table is present, TO at 10 sec
    expected_table = wait.until(EC.presence_of_element_located((By.ID, 'DataTable')))

    # make some soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # find table
    table = soup.find("table", {'id': 'DataTable'})
    # print(table)

    headers = [header.text.strip() for header in table.find_all("th")]
    rows = table.find_all("tr")[1:] # skipping header row

    data = []
    for row in rows:
        tds = [td.text.strip() for td in row.find_all("td")] # grab text from different tds
        output = ""
        for i in range(len(headers)):
            output += f"{headers[i]}: {tds[i]}"
            if i < len(headers) - 1:
                output += ", "
        data.append(output)

    return data