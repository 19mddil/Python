import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data.decode())
comments = tree.findall('./comments/comment')
print('Count:',len(comments))
print('Sum:',sum([int(comment.find('count').text) for comment in comments]))
