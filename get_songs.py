import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.vagalume.com.br/'

def getSongs(band):
    response = requests.get(baseUrl + band)
    
    if response.status_code != 200:
        print('erro')
    
    parsed_html = BeautifulSoup(response.content, features='lxml')
    musics = parsed_html.body.find('ol', id='alfabetMusicList')
    for song_tag in musics.find_all('li'):
        song = song_tag.find('a')

        if song is not None and 'href' in song.attrs:
            link_song = song.attrs['href']
            getLyric(song.text, link_song)


def getLyric(song, link_song):
    response = requests.get(baseUrl + link_song)
    
    if response.status_code != 200:
        print('erro')

    parsed_html = BeautifulSoup(response.content, features='lxml')
    lyric = parsed_html.find(id='lyrics')

    if(lyric.text.find('the another') > 0):
        print(f"{song} - the another")

    elif(lyric.text.find('another') > 0):
        print(f"{song} - another")

    elif(lyric.text.find('the others') > 0):
        print(f"{song} - the others")

    elif(lyric.text.find(' other') > 0):
        print(f"{song} - other")

getSongs('creed')