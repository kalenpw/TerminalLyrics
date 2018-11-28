import re
import urllib.request
from bs4 import BeautifulSoup

def getAmountOfChar(amount, char):
    printStatement=""
    for i in range(0, amount):
        printStatement += char
    return printStatement
 
def get_lyrics(artist, song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    # remove starting 'the' from artist e.g. the who -> who
    if artist.startswith("the"):    
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').replace('<br/>', '').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)

artist_name = input("Enter artist\n")
song_name = input("Song title\n")
titleLength = len(artist_name) + len(song_name) + 1
print(getAmountOfChar(titleLength, '#'))
print('\n' + artist_name + '-' + song_name + '\n')
print(getAmountOfChar(titleLength, '#'))
print(get_lyrics(artist_name, song_name))
