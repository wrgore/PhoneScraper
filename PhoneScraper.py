#!/bin/python3
#import data based on area code input

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

#Takes input from user for their desired area code. Wordlist will be generated based on this.
areacode = input ("Enter the area code you would like to make a wordlist for. Use the following format '123'. \n")

#Read the webpage for the specified area code. This code pretends to be a browser to allow for scraping.
req = Request('!!!URL goes here!!!' + areacode, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#Parse and clean html down to the content we want.
soup = BeautifulSoup(webpage, 'html.parser')
group = soup.find_all("div", attrs={"class": "list-group-item"})

#Print cleaned data to a text file and close for later.
rawareacodes = open("output.txt","a")
print (group, file=rawareacodes)
rawareacodes.close

#REGEX to find area codes + prefixes in the data.
data = open("output.txt","r")
read = data.read()
data = re.findall('\(\d{3}\)\s\d{3}', read)
print (data)
