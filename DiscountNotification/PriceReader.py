from bs4 import BeautifulSoup
import urllib.request

def removeComma(s):
	s = s.split(",")
	return "".join(s)

x = urllib.request.urlopen('https://www.amazon.in/Apple-iPhone-Silver-64GB-Storage/dp/B0711T2L8K/ref=sr_1_2?s=electronics&ie=UTF8&qid=1540612639&sr=1-2&keywords=iphone')
soup =BeautifulSoup(x,'html.parser')
a = soup.find('span',id='priceblock_dealprice')
price=a.text
price = (removeComma(price))
price=float(price)
print(price)
