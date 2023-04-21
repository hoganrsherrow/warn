import csv
import requests
from io import StringIO


def scrape_web_co(sheet_id="1gsLtXhwCIqFUg1I9PZwX4hmSPmxi5ra4PmOzA99Eg28", gid="1113945780"):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    response = requests.get(url)
    response.raise_for_status()
    csv_file = StringIO(response.text)

    reader = csv.reader(csv_file)
    headers = next(reader)  # Get headers from the first row
    formatted_data = []

    for row in reader:
        # Stop processing if the row is completely empty
        if all(cell == '' for cell in row):
            break

        formatted_row = {}
        for i, value in enumerate(row):
            formatted_row[headers[i]] = value
        formatted_data.append(formatted_row)

    return formatted_data
