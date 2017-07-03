'''this is the code I need to utilize to pull information on
trending stocks from Seeking Alpha -- it is ONLY for Non-Commercial
Personal use'''
from bs4 import BeautifulSoup

# need to go to the XML trending analysis site for SKNAlpha
# https://seekingalpha.com/listing/most-popular-articles.xml

trending = BeautifulSoup('https://seekingalpha.com/listing/most-popular-articles.xml'
, 'lxml')

print("here is the link:")
print (trending)

print("looking for the various symbols:")
for category in trending.find_all(True):
    print(category.name)
print("this worked.")
