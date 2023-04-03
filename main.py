import extract
import web_scraper

# TN WARN
url = "https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/reports.html"

findings = web_scraper.scrape_web(url=url)

for finding in findings:
    print(extract.extract_information(text=finding, model_path="outputmodels/model1"))
