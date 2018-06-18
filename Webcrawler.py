from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/global/sg/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=video+card&N=-1&isNodeId=1'

# Opening up connection, grabbing the page
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
title_container = page_soup.findAll("a", {"class": "item-title"})
shipping_container = page_soup.findAll("li", {"class": "price-ship"})
fileName = "product.csv"
f = open(fileName, "w")

headers = "Brand, product name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    itemName = title_container[0].text

    shipping = shipping_container[0].text

    f.write(brand + "," + itemName.replace(",", "|") + "," + shipping + "\n")

f.close()
