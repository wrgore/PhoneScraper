#!/bin/python3
#import data based on area code input

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os

#Print warning that the script will create and remove a file called scripttemp.txt.
warning = input ("This script will create and then delete a file called scripttemp.txt in the running directory. Would you like to continue (Y/N?)\n")
if warning == "Y":
    print ("Input accepted, continuing script.")
elif warning == "N":
    print ("Input accepted. Script will be halted.")
    exit()
else:
    print ("Invalid input. Script will be halted.")
    exit()

#Takes input from user for their desired area code. Wordlist will be generated based on this.
areacode = input ("Enter the area code you would like to make a wordlist for. Use the following format '123'. \n")

#Read the webpage for the specified area code. This code pretends to be a browser to allow for scraping.
req = Request('https://www.allareacodes.com/' + areacode, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#Parse and clean html down to the content we want.
soup = BeautifulSoup(webpage, 'html.parser')
group = soup.find_all("div", attrs={"class": "list-group-item"})

#Print cleaned data to a text file and close for later.
with open ("scripttemp.txt","a") as rawareacodes:
    print (group, file=rawareacodes)
    rawareacodes.close

#REGEX to find area codes + prefixes in the data.
with open ("scripttemp.txt") as file:
    read = file.read()
    data = re.findall('\(\d{3}\)\s\d{3}', read)
    file.close

#Trim data to just a list of numbers.
data = [data.replace("(","")for data in data]
data = [data.replace(")","")for data in data]
data = [data.replace(" ","")for data in data]
#print (data)

#Open file for final output and iterate through data.
output = open(areacode+".txt","a")

i = 0000
print ("Creating wordlist. This should take approximately 60 seconds.")

for n in data:
    for i in range (0000, 10000):
        print (str(n)+'{0:04}'.format(i), file=output)

#Clean up files and finish script.
print ("Cleaning up files...")
os.remove("scripttemp.txt")
print ("Dataset creation successful.")
