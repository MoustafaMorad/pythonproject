import requests
from bs4 import BeautifulSoup as bss4
url=requests.get("https://ar.newchic.com/mens-clothing-c-3581/?country=63&AR=0")
soup =bss4(url.text,'html.parser')
product_name = soup.findAll('a',{'class':'lg text-ellipsis d-block text-hover-underline text-secondary-hover font-small-12 text-grey product-item-name-js'})

for i in range(len(product_name)):

    print(product_name[i].text)