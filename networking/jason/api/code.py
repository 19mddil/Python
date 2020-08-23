import urllib.request,urllib.parse,urllib.error
import json
import ssl

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

api_key = 'AIzaSyD7wQw5k5yfXckF9KNp7KMTuqwux_0OA5Y'

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocde/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print(data)
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print(data)
        continue

    print(json.dumps(js,indent=4)) #printing the json
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)
