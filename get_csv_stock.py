from bs4 import BeautifulSoup
from time import sleep
import requests


if __name__ == '__main__':
    url = requests.get('https://asic.gov.au/regulatory-resources/markets/short-selling/short-position-reports-table/').text
    soup = BeautifulSoup(url)
    for link in soup.findAll("a"):
        current_link = link.get("href")
        if current_link.endswith('csv'):
            print('Found CSV: ' + current_link)
            print('Downloading %s' % current_link)
            response = requests.get('https://asic.gov.au%s' % current_link, stream=True)
            fn = current_link.split('/')[-3] + '_' + current_link.split('/')[-2] + '_' + current_link.split('/')[-1]
            print(fn)
            with open(fn, "wb") as handle:
                for data in response.iter_content():
                    handle.write(data)