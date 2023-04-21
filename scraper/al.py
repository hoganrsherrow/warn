from bs4 import BeautifulSoup
import requests

def scrape_web_al(url="https://www.madeinalabama.com/warn-list/"):
    print("Grabbing Alabama layoff data...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    headers = [th.text.strip() for th in table.find_all('th')]

    data = []

    for row in table.find_all('tr')[1:]:
        tds = [td.text.strip() for td in row.find_all('td')]
        row_data = ', '.join([f"{header}: {value}" for header, value in zip(headers, tds)])
        data.append(row_data)

    return data