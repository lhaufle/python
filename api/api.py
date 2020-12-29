import requests

class API:

    url = 'https://bible-api.com/'
    translation = '?translation=kjv'
    verse = ""

    def __init__(self, bible):
        self.bible = bible #hold bible verse
        self.verse = self.url + self.bible + self.translation #build url string with verse

    def get_request(self):
        req = requests.get(self.verse)
        if req.status_code != 200:
            print("Problem with Api request")
        else:
            values = req.json() #create dictionary object
            txt = values['text'].strip() #clean up the space around the text
            print('\n') #create some space
            print(txt)
            print('-----------' + self.bible + ' KJV' + '-----------')
