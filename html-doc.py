from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

#print(doc.prettify()) #html yada xml dosyalarının daha okunaklı olması için

tag = doc.title # <title> ve </title> bloğu içinde ki bölümü almak için
#print(tag.string) #blokları görmemek için

tag_a = doc.find("a") #<a> .... </a> bloğunu aramak için
#print(tag_a)

tag_p = doc.find("p") #<p> ... </p> bloğunu aramak için
#print(tag_p)

tags = doc.find_all("p")[0]
print(tags.find_all("b"))
