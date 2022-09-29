import requests 
from bs4 import BeautifulSoup
from time import sleep

content = ''

def get_miles(url):
    result = []
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all('div', attrs={"class":"css-1dbjc4n r-xoduu5 r-1iusvr4 r-16y2uox r-1wbh5a2"}):
        result.append(i.text)
        #print(i.text)
    return result

cnt = get_miles("https://app.ironmanvirtualclub.com/en/dashboard")

for row in cnt:
    print(row)
    sleep(0.5)

#class = "css-901oao css-16my406 r-1vprpcz r-1eo6hi2 r-1b43r93 r-b88u0q r-knv0ih"