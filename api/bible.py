from api import API

#to hold api input or be used as a flag to kill the loop
verse = ''

while verse != 'x':
    #get verse from user
    verse = input("Please enter for Book name with chapter and verse like John 3:16 or press x to quit::")
    #kill job before running api request
    if verse == 'x':
        break
    #initialize object with verse
    bible_request = API(verse)
    #send get request and print response
    bible_request.get_request()

print("Good Bye")
