# import bs4
from bs4 import BeautifulSoup
import requests

# TN WARN notices
url = "https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/reports.html"

response = requests.get(url)
html = response.content

# make some soup
soup = BeautifulSoup(html, 'html.parser')

# find all <p> tags under id='main' div
main_div = soup.find('div', {'id': 'main'})
p_tags = main_div.find_all('p')

# output content

print("=== TN WARN Act Results ===\n")

for p_tag in p_tags:
    print(p_tag.text)

print("\n=== TN WARN Act Results End ===\n")

