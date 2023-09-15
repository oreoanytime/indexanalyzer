import re, requests, json, csv
from io import StringIO
from bs4 import BeautifulSoup

def scrape_data():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    index = "GSPC"

    hist_data = f'https://query1.finance.yahoo.com/v7/finance/download/%5E{index}?'
    params = {
        'range':'5y',
        'interval':'1d',
        'events':'history'
    }

    response = requests.get(hist_data, params=params, headers=headers)

    file = StringIO(response.text)
    reader = csv.reader(file)
    data = list(reader)

    return data

# data = scrape_data()

# print(f"Number of rows: {len(data)}")

# for row in data[-5:]:
#     print(row)
