import requests
import json
import youtube_dl
api_key = "KEY GOES HERE"
#def user_playlist(channel):
    #url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+ channel + "&key="+ api_key
    #r = requests.get(url)
    #print(r.json)
print("init")
channel = "vsauce2"
url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+ channel + "&key="+ api_key
r = requests.get(url)
ydl = r.text
ydl = json.loads(ydl)
print(ydl["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"])
