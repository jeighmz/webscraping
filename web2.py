import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import datetime
import argparse

from time import sleep
from tqdm import tqdm

now = datetime.datetime.now()

parser = argparse.ArgumentParser()


s = HTMLSession()
content = ''

## optional parameters
parser.add_argument('--count', type=int, required=False)
args = parser.parse_args()


def extract_news(url):
    token = []
    prices = []
    prices_copy = []
    response = s.get(url)
    #alternate method: requests
    ##content = response.content
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('td', attrs={'class': "td-price price text-right", 'data-no-decimal': ''}, limit = args.count):
        prices.append(i.text)
    for j in soup.find_all('span', attrs={'class':"lg:tw-flex font-bold tw-items-center tw-justify-between"}, limit = args.count):
        token.append(j.text)
    result = []
    #cleaning
    for elements in prices:
        e = elements.replace('\n', '')
        prices_copy.append(e)

    prices = prices_copy
    
    if len(prices) == len(token): 
        print("Retrieving Real-time Crypto Data...\n")
    else:
        print("Something's Wrong")
        print("Check lengths: " + len(prices), len(token))
    for i in tqdm(range(len(prices))):
        result.append( token[i][:-1] + ': ' + prices[i] )
    
    return result


cnt = extract_news('https://www.coingecko.com')

for row in cnt:
    print(row)
    sleep(0.35)
