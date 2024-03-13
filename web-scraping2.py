from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

#modify document

result = doc.find_all("h1") #bulunan tüm h1'e ait ögeyi
tag = doc.find("option") #bulunan ilk h1 etiketine ait ögeyi
# tag['selected'] = 'false' #option etiketinde ki selected ögesini false olarak değiştirir
# tag['color'] = "blue"
print(tag)
print(tag.attrs) #nesneye ait özellikler

# tags = doc.find_all(["p", "div", "li"]) #<p>, <div>, <li> blokları
# print(tags)
#
# tagss = doc.find_all(["a"], string="Example Link 1") #<a> bloğunda ki stringleri arar ama eksik yazdığın zaman boş küme dönüyor, stringi tam yazmalısın
# print(tagss)
#
#
# tagss_1 = doc.find_all(class_ = "button")
# print(tagss_1)
#
# tagss_2 = doc.find_all(string=re.compile("\$.*")) #karakter araman için \ . * koyman gerekir
# for tag in tagss_2:
#     print(tag.strip())
#
# tagss_3 = doc.find_all("input", type="text")
# for tag in tagss_3:
#     print(tag.strip())
#
# with open("changed.html", "w") as file:
#     file.write(str(doc))

