import json
import re
import requests
from bs4 import BeautifulSoup
api_key = "AIzaSyBsMBJGUeWk_a0zHE9TpJWBZHV6mkzwG3A"

class YouTubeStatus:
    def __init__(self, url: str):
        self.json_url = requests.get(url)
        self.data = json.loads(self.json_url.read())

        def print_data(self):
            print(self.data)
        def get_video_titel(self):
            return self.data["items"][0]["snippet"]["titel"]
        def get_video_description(self):
            return self.data['items'][0]['snippet']['descrition']

#skriv inn url for å få html koden til netsiden
"""lager videoid for YT_api og nettside for selenium"""
nettside = 'https://www.youtube.com/watch?v=RHQC4fAhcbU'
video_id = nettside.split("=")[1]
#url = "www.example.com
#new_url = url[:url.rfind(".")]
print(video_id)
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
sorce = requests.get(nettside).text


class Helper_url:
    def __init__(self):
        pass
    def title_to_underscore_title(self, title: str):
        title = re.sub('[/W_]+', "_", title)
        return title.lower()
    def id_from_url(self, url: str):
        return url.rsplit("/", 1)[1]

#gi titler store bokstaver
def titlecase(s):
     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                   lambda mo: mo.group(0).capitalize(),
                   s)
