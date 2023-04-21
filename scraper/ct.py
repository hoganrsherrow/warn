import requests
from bs4 import BeautifulSoup

def scrape_web_ct(url="https://www.ctdol.state.ct.us/progsupt/bussrvce/warnreports/warn2023.htm"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.find_all('table')
    # for i, table in enumerate(tables):
    #     print(f"==================== Table {i} ================\n{table}\n======================================================================")
    rows = tables[7].find_all('tr')
    headers = [header.text.strip() for header in rows[0].find_all('td')]

    data = []
    
    for row in rows[1:]:
        tds = [td.text.strip() for td in row.find_all('td')]
        row_data = ', '.join([f"{header}: {value}" for header, value in zip(headers, tds)])
        data.append(row_data)

    return data