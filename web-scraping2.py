from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

#result = doc.find_all("h1") #bulunan tüm h1'e ait ögeyi
tag = doc.find("h1") #bulunan ilk h1 etiketine ait ögeyi
tag['value'] = 'new value'
print(tag)