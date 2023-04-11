from bs4 import BeautifulSoup
import requests

def scrape_web_TN(url="https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/reports.html"):
    print("Grabbing TN web results...")
    response = requests.get(url)
    html = response.content

    # make some soup
    soup = BeautifulSoup(html, 'html.parser')

    # find all <p> tags under id='main' div
    main_div = soup.find('div', {'id': 'main'})
    p_tags = main_div.find_all('p')

    results = []
    # iterate through the p_tags
    for p_tag in p_tags:
        results.append(p_tag.text.replace('\xa0', ' '))
    return results