import requests 
from bs4 import BeautifulSoup
from time import sleep
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--topic', type=str, required=True)

args = parser.parse_args()

content = ''

def get_articles(url):
    result = []
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all('h2', attrs={'class':'title'}):
        result.append(i.text)
        #print(i.text)
    return result

cnt = get_articles('https://www.npr.org/sections/{args}/'.format(args=args.topic))

for row in cnt:
    print(row)
    sleep(0.5)

