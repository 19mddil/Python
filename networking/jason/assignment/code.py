import urllib.request, urllib.parse, urllib.error
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ');
print('Retrieving',url)
content = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved',len(content),'characters')
json_content = json.loads(content)
#print(json.dumps(json_content,indent=4))
print('Count:',len(json_content['comments']))
print('Sum:',sum([item['count'] for item in json_content['comments']]))
