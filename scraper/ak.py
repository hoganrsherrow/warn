import requests
from bs4 import BeautifulSoup

def scrape_web_ak(url="https://jobs.alaska.gov/rr/WARN_notices.htm"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table')
    rows = table.find_all('tr')
    headers = [header.text.strip() for header in rows[0].find_all('td')]

    data = []
    
    for row in rows[1:]:
        tds = [td.text.strip() for td in row.find_all('td')]
        row_data = ', '.join([f"{header}: {value}" for header, value in zip(headers, tds)])
        print(row_data)
        data.append(row_data)

    return data