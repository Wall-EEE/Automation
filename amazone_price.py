import requests
from bs4 import BeautifulSoup
import re
list_name = []
list_price = []
# loope over en liste med nettsider, kanskje igjenom chromeium
URL = "https://www.amazon.de/dp/B07KMV94JF/ref=sr_1_2?keywords=ps4&qid=1582233936   &rnid=1703609031&s=videogames&sr=1-2"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")
name = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text().replace("\xa0","")
#print(soup.prettify())
list_name.append(name)
list_price.append(price)
print(list_name)
print(list_price)

#for i in range(10):
#
#if page.status_code != 200:
#        print("Error status code: " + str(page.status_code))
#        continue



#mostwant = soup.find(id="priceblock_ourprice").get_text()
#griditem = soup.find(class_="a-size-medium a-color-price").get_text()
#divs = soup.findAll(attrs = mostwant) + soup.findAll(attrs = griditem)
#for product in divs:
#    item = product.h2.a.text.strip()
#    price = re.search('\d+\.\d+', product.findAll('p')[1].text).group(0)
#    print(f"{item} - {price}")
#
#