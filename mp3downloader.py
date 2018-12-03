import urllib
import urllib.parse
import urllib.request
from urllib.request import urlretrieve
import requests
import sys
from bs4 import BeautifulSoup
import urllib.error
from selenium import webdriver
from seleniumrequests import Firefox

#driver = Firefox()
url = 'http://www.mp3int.com/search.php'
song = input("Enter song name: ")
data = {'search':song}
data = urllib.parse.urlencode(data)
data = data.encode('ascii') #data must be converted into bytes form

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req).read()#get the bytes in payload
soup = BeautifulSoup(resp,"html.parser")#get the html page
divs = soup.find_all("div","topbox") #get div elements with class = "topbox"
divL = []
for tag in divs:
    divL.append(tag.attrs)
no_of_songs_found =  len(divL)
if no_of_songs_found==0:
    print("Nothing found!!")
    sys.exit(0)
try:    
    for i in range(no_of_songs_found):
        print("index: ",i,"name: ",divL[i]['name'])
except:
    print("\nException occured")
index = int(input("enter index: "))
name = input("enter name of file to be saved as: ")
name = name + '.mp3'
url_download = 'http://www.mp3int.com/downloadmp3.php?'+'rdvidid='+divL[index]['id']+'&rdvidnm='+divL[index]['name']
print(url_download)
trial = 0
executed = False
while not executed:
    
    #element = driver.find_element_by_id(divL[index]['id'])
    #element.click()
    trial += 1
    print("attempt:",trial)
    if trial>10:
        executed = True
    try:
        print(url_download)
        urlretrieve(url_download,name)
        executed = True
        print("File downloaded!! check your Python directory")
    except urllib.error.HTTPError as err:
        print(err)

