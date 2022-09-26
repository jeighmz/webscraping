import requests
from bs4 import BeautifulSoup
import datetime

from time import sleep
from tqdm import tqdm

now = datetime.datetime.now()

content = ''

def extract_news(url):
    token = []
    prices = []
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all('div', attrs={'class': "sc-131di3y-0 cLgOOr", 'style':''}):
        prices.append(i.text)
    for j in soup.find_all('p', attrs={'class' : 'sc-1eb5slv-0 iworPT', 'font-size': '1'}):
        token.append(j.text)

    result = []

    if len(prices) == len(token): 
        print("Retrieving Real-time Crypto Data...\n")
    else:
        #print("Adjusting...")
        token = token[6:]
        print("Retrieving Real-time Crypto Data...")

    for i in tqdm(range(len(prices))):
        result.append( token[i] + ': ' + prices[i] )
    
    return result


cnt = extract_news('https://coinmarketcap.com')

for row in cnt:
    print(row)
    sleep(0.5)
