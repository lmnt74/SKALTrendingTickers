'''this is the code I need to utilize to pull information on
trending stocks from Seeking Alpha -- it is ONLY for Non-Commercial
Personal use'''
from bs4 import BeautifulSoup
# from BeautifulSoup import BeautifulStoneSoup as Soup

from lxml import etree
from lxml import html
import requests
import itertools
import pandas

# need to go to the XML trending analysis site for SKNAlpha
# https://seekingalpha.com/listing/most-popular-articles.xml

# put URL into URL
url = 'https://seekingalpha.com/listing/most-popular-articles.xml'

#just to print onto terminal - can comment out /delete later
print('URL via just print')
print(url)

# this puts the page url into the variable page
page = requests.get(url)
#create the tree element to hold the text of the xml file
tree = page.text

#parse the xml to get the links for the symbols
soup = BeautifulSoup(tree,"xml")


#printing out links, need to parse out just symbols
print("looking for the various symbols:")
symbols = []
# i = 0

for category in soup.findAll('category', {'type' : 'symbol'}):
    symbols.append(category.string)
    # i += 1

symbols.groupby('symbols').count.nunique
#count the number of symbols in trending articles



print("program has finished")
