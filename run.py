import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    contents = requests.get(url, params={'tag_from': 'framebar'})

    soup = BeautifulSoup(contents.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = populer_area.findAll(attrs={'class': 'media__title'})
    # menampilkan judul
    # for judul in titles:
    # print(judul.text)

    images = populer_area.findAll(attrs={'class': 'media__image'})

    return render_template('hasilscrap.html', images = images )










if __name__ == '__main__':
    app.run(debug=True)