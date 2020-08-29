import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
f = False

for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    if where == 'Plot # 77-78, Road # 9, Rupnagar R/A Mirpur-2 Dhaka, Dhaka 1216, Bangladesh':
        print("\n\tHighlighted Start")
        f = True

    try :
        if f:
            print('\t\t',where, lat, lng)
        else:
            print(where,lat,lng)
        if where == 'Plot # 77-78, Road # 9, Rupnagar R/A Mirpur-2 Dhaka, Dhaka 1216, Bangladesh':
            print("\tHighlighted End\n")

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

