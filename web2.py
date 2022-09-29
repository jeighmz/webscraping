import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import datetime

from time import sleep
from tqdm import tqdm

now = datetime.datetime.now()

s = HTMLSession()
content = ''

def extract_news(url):
    token = []
    prices = []
    prices_copy = []
    response = s.get(url)
    #content = response.content
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('td', attrs={'class': "td-price price text-right", 'data-no-decimal': ''}):
        prices.append(i.text)
    for j in soup.find_all('span', attrs={'class':"lg:tw-flex font-bold tw-items-center tw-justify-between"}):
        token.append(j.text)
    #print(prices)
    # for elements in prices:
    #     if '.' not in elements:
    #         prices.remove(elements)
    #     else:
    #         prices2.append(elements)
    #print(token)
    #print(len(token), len(prices))
    result = []
    for elements in prices:
        e = elements.replace('\n', '')
        prices_copy.append(e)

    prices = prices_copy
    if len(prices) == len(token): 
        print("Retrieving Real-time Crypto Data...\n")
    else:
        #print("Adjusting...")
        #token = token[6:]
        print("Retrieving Real-time Crypto Data...")
    for i in tqdm(range(len(prices))):
        result.append( token[i][:-1] + ': ' + prices[i] )
    
    return result


cnt = extract_news('https://www.coingecko.com')

for row in cnt:
    print(row)
    sleep(0.35)
