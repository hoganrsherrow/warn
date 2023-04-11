from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def scrape_web_WA(url="https://fortress.wa.gov/esd/file/warn/Public/SearchWARN.aspx"):
    driver = webdriver.Chrome()
    driver.get(url)

    page_number = 1

    while True:  # Loop through all the pages
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')

        # table headings
        headers = []
        th_tags = body.find_all('th')
        for th in th_tags:
            headers.append(th.text)

        print(f"Headers... {headers}")

        # find text
        tr_tags = body.find_all('tr')
        for tr_tag in tr_tags:
            tr_str = ""
            td_tags = tr_tag.find_all('td')
            if len(td_tags) == len(headers):
                for i in range(len(td_tags)):
                    tr_str += headers[i]
                    tr_str += ": "
                    tr_str += td_tags[i].text.strip()
                    tr_str += " "
            tr_str += "State: WA"
            print(tr_str)

        # Find the next page number link
        page_number += 1
        try:
            next_page_link = driver.find_element("xpath", f'//a[@href="javascript:__doPostBack(\'ucPSW$gvMain\',\'Page${page_number}\')"]')
        except NoSuchElementException:
            break  # Exit the loop if there is no next page number link

        if next_page_link:
            next_page_link.click()  # Click the next page number link