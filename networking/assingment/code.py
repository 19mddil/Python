import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def twk( url ,pos):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    #lnk = tags[pos-1].decode()
    lnk = tags[pos-1].get('href',None)
    return lnk

starting_url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
temp = None
for i in range(count):
    if temp is None:
        temp = starting_url
        print('Retrieving:',temp)
    #temp = re.findall('href="(.+)"',twk(temp,position))[0]
    temp = twk(temp,position)
    print('Retrieving:',temp)
