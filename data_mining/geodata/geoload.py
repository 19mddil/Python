import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1
flag = False
f = False
try:
    conn = sqlite3.connect('geodata.sqlite')
    flag = True
except:
    sys.exit(0)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 400 :
        print('Retrieved 400 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if address == 'Bangladesh University of Business and Technology (BUBT)':
        print("\tHighlighted Start")
        f = True
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    if f:
        print('\t\tRetrieving', url)
    else:
        print('Retrieving',url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    if f:
        print('\t\tRetrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    else:
        print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    if address == 'Bangladesh University of Business and Technology (BUBT)':
        print("\tHighlighted End\n")

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
conn.commit()
if flag: 
    print("Created geodata.sqlite")
    cur.execute('select count(address) from Locations')
    print(str(cur.fetchone()[0])," entris in geodata.sqlite")
cur.close()

#print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
