# webscraping with BeautifulSoup4 Python 3.10 package. 

BeautifulSoup4 is a package that allows for information to be scraped
directly off of the website. After performing a get request with 
built-in python package requests, the url is broken apart with an HTML parser:

    soup = BeautifulSoup(content, 'html.parser')
    
With a for loop going through the method .find_all(object, attrs={}), 
text can be accessed through the iterator variable.

    for i in soup.find_all('div', attrs={'class': "title"}):
        print(i.text)

web2.py
Real-time cryptocurrency price checker  #sourced from CoinMarketCap.

Packages:
- BeautifulSoup
- requests
- datetime
- tqdm
- sleep

web3.py
Current events news headlines by category #sourced from NPR.

Packages:
- argparse
- repeat web2.py
