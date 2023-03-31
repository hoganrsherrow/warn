# import bs4
from bs4 import BeautifulSoup
import requests
import nltk
import re
import spacy
import json

# TN WARN notices
url = "https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/reports.html"

response = requests.get(url)
html = response.content

# make some soup
soup = BeautifulSoup(html, 'html.parser')

# find all <p> tags under id='main' div
main_div = soup.find('div', {'id': 'main'})
p_tags = main_div.find_all('p')

### NLP ###
# load English language model for spaCy
nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')

def extract_warn_info(text):
    pattern = r"Date Notice Posted: (\d{4}/\d{1,2}/\d{1,2}) \| Company: (.*?) \| County: (.*?) \| Affected Workers: (\d+) \| Closure/Layoff Date: (.*?) \| Notice/Type: #(.*?)"

    matches = re.findall(pattern, text)
    for match in matches:
        date_notice_posted, company, county, affected_workers, closure_layoff_date, notice_type = match
        result_map = {
            "Date Notice Posted": date_notice_posted,
            "Company": company,
            "County": county,
            "Affected Workers": affected_workers,
            "Closure/Layoff Date": closure_layoff_date,
            "Notice/Type": notice_type
        }
        print(result_map)
        results.append(result_map)

def write_json_file(results_arr):
    output = {
        "results": results_arr
    }
    with open("results.json", "w") as json_file:
        json.dump(output, json_file)

# output content
print("=== TN WARN Act Results ===\n")
my_tags = []
results = []
for p_tag in p_tags:
    p_text = p_tag.text
    my_tags.append(p_text.replace('\xa0', ' '))
    extract_warn_info(p_text.replace('\xa0', ' '))
print(my_tags)
print(results)
print("\n=== TN WARN Act Results End ===\n")

print("\nCreating JSON file...\n")
write_json_file(results)
print("results.json has been created.\n")