#!/bin/python3
#import data based on area code input

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#Takes input from user for their desired area code. Wordlist will be generated based on this.
areacode = input ("Enter the area code you would like to make a wordlist for. Use the following format '123'. \n")

#Read the webpage for the specified area code. This code pretends to be a browser to allow for scraping.
req = Request('YOULL NEED TO INPUT YOUR PREFERRED SITE HERE' + areacode, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
data = BeautifulSoup(webpage, 'html.parser')

#Print the full page output to a file called rawareacodes.
rawareacodes = open("output.txt", "a")
print (data, file=rawareacodes)
rawareacodes.close
print("Scrape successful")
