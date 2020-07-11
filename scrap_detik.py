import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
contents = requests.get(url,params={'tag_from':'framebar'})

soup = BeautifulSoup(contents.text,'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})
titles = populer_area.findAll(attrs={'class':'media__title'})
# menampilkan judul
# for judul in titles:
    # print(judul.text)

image = populer_area.findAll(attrs={'class':'media__image'})
# menampilkan gambar
for gambar in image:
    print(gambar.find('a').find('img')['title'])

# print(titles)
