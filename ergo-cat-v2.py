#Ergo Cat is a countdown timer in Python that opens a cat gif on giphy.com at the end of the countdown.

#Ergo Cat's job is to interrupt you so that you take a break from staring at your screen for too long. 

#import url library
import webbrowser

#import time, allows us to use time functions
import time

#set countdown time in seconds
seconds = int(1200)

#ranged loop to count downwards 
for i in range(seconds):
    print (str(seconds - i) + " seconds remain")
    #have Python pause for 1 second between each iteration
    time.sleep(1)

print('Ergo Cat says "Time is up!"')

#import url and json libraries so we can get a random cat gif
import urllib, json

# this is the url to get a random gif data from
randomCatFetchURL = "http://api.giphy.com/v1/gifs/random?api_key=GUCeL1CQLcZdYsiIkRkfwOMvBL9lJoza&tag=cat"
response = urllib.urlopen(randomCatFetchURL)

# now 'data' holds the info about the random gif url we want.
data = json.loads(response.read())

# access the `data` dictionary to get the random url
randomGifURL = data["data"]["url"]

#go to web page in a new window, though most of the time it just opens in a new tab
webbrowser.open(randomGifURL + "/fullscreen", new=1, autoraise=True)
