from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import openpyxl
from io import BytesIO

def scrape_web_KY(url="https://kcc.ky.gov/Pages/News.aspx"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    base_url = "https://kcc.ky.gov"
    
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        xlsx_links = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True) if a ['href'].endswith('.xlsx')]

        for xlsx_link in xlsx_links:
            response = requests.get(xlsx_link, headers=headers)

            workbook = openpyxl.load_workbook(BytesIO(response.content))

            sheet = workbook.active
            col_headers = [cell.value for cell in sheet[1]]

            print(f"Contents of {xlsx_link}:")
            for row in sheet.iter_rows(min_row=2, values_only=True):
                row_str = ""
                for header, value in zip(col_headers, row):
                    row_str += f"{header}: {value}, "
                print(row_str)
            print()
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}, Reason: {response.reason}")