import requests
from io import BytesIO
import pdfplumber

def scrape_web_CA(url="https://edd.ca.gov/en/Jobs_and_Training/Layoff_Services_WARN"):
    # driver = webdriver.Chrome()
    # driver.get(url)

    # time.sleep(5)
    # html = driver.page_source
    # driver.quit()

    # soup = BeautifulSoup(html, 'html.parser')
    # pdf_link = soup.find("a", href=lambda href: href and href.endswith(".pdf"))["href"]
    pdf_link = "https://edd.ca.gov/siteassets/files/jobs_and_training/pubs/warn-report-for-7-1-2021-to-06-30-2022.pdf"
    
    # download the pdf file
    pdf_response = requests.get(pdf_link)
    pdf_file = BytesIO(pdf_response.content)

    # process the PDF using pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            table=page.extract_table()
            for row in table:
                print(f"Notice Date: {row[0]}, Effective Date: {row[2]}, Company: {row[3]}, Affected Workers: {row[5]}, {row[4]}")