# import bs4
from bs4 import BeautifulSoup
import requests
import nltk
import re
import spacy

# TN WARN notices
url = "https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/reports.html"

response = requests.get(url)
html = response.content

# make some soup
soup = BeautifulSoup(html, 'html.parser')

# find all <p> tags under id='main' div
main_div = soup.find('div', {'id': 'main'})
p_tags = main_div.find_all('p')

my_text = """
Date Notice Posted: 2018/10/19 | Company: Goodman Manufacturing Company L.P. | County: Lincoln | Affected Workers: 81 | Closure/Layoff Date: December 21, 2018 | Notice/Type: #20180032
Date Notice Posted: 2018/10/11 | Company: GSK Consumer Health - Global manufacturing & Supply | County: Shelby | Affected Workers: 99 | Closure/Layoff Date: December 10, 2018 | Notice/Type: #20180031
Date Notice Posted: 2018/9/28 | Company: Youth Villages | County: Perry | Affected Workers: 87 | Closure/Layoff Date: November 
25, 2018 | Notice/Type: #20180030
Date Notice Posted: 2018/9/14 | Company: LGSTX Distribution Services | County: Shelby | Affected Workers: 177 | Closure/Layoff 
Date: September 30, 2018 | Notice/Type: #20180029
Date Notice Posted: 2018/9/7 | Company: Fred's Inc. | County: Shelby | Affected Workers: 80 | Closure/Layoff Date: October 28, 
2018 | Notice/Type: #20180028
Date Notice Posted: 2018/9/5 | Company: Kayser-Roth Corporation | County: Rhea | Affected Workers: 85 | Closure/Layoff Date: November 5, 2018 | Notice/Type: #20180027
Date Notice Posted: 2018/8/7 | Company: Caterpillar Inc. | County: Dyer | Affected Workers: 85 | Closure/Layoff Date: October 1, 2018 | Notice/Type: #20180026
Date Notice Posted: 2018/7/12 | Company: Cantech Industries, Inc. | County: Washington | Affected Workers: 68 | Closure/Layoff 
Date: September 10, 2018 | Notice/Type: #2018025
Date Notice Posted: 2018/7/12 | Company: The Fresh Market | County: Sumner | Affected Workers: 61 | Closure/Layoff Date: August 3, 2018 | Notice/Type: #2018024
Date Notice Posted: 2018/6/21 | Company: Jackson National Life Insurance | County: Williamson | Affected Workers: 64 | Closure/Layoff Date: June 15, 2018, July 6, 2018, August 3, 2018 | Notice/Type: #2018023
Date Notice Posted: 2018/6/15 | Company: Xanitos Inc. | County: Hamilton | Affected Workers: 156 | Closure/Layoff Date: August 
18, 2018 | Notice/Type: #2018022
Date Notice Posted: 2018/6/11 | Company: Adient US LLC | County: Giles | Affected Workers: 54 | Closure/Layoff Date: July 31, 2018 | Notice/Type: #20180021
Date Notice Posted: 2018/6/4 | Company: Incipio Group | County: Rutherford | Affected Workers: 48 | Closure/Layoff Date: July 31, 2018 | Notice/Type: #20180020"""

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
    # Return the data as a dictionary
    # return {
    #     "Date Notice Posted": date_notice_posted,
    #     "Company": company,
    #     "County": county,
    #     "Affected Workers": affected_workers,
    #     "Closure/Layoff Date": closure_layoff_date,
    #     "Notice/Type": notice_type
    # }

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