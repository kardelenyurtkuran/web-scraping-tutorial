from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")


print(doc.prettify()) #html yada xml dosyalarının daha okunaklı olması için

tag = doc.title # <title> ve </title> bloğu içinde ki bölümü almak için
print(tag.string) #blokları görmemek için

tags = doc.find_all("a") #<a> .... </a> bloğunu aramak için
print(tags)

tag_p = doc.find_all("p") #<p> ... </p> bloğunu aramak için
print(tag_p)

tags = doc.find_all("p")[0]
print(tags.find_all("b"))
