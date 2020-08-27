import sqlite3
import re

conn = sqlite3.connect('org.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = re.findall('@(.+)',email)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[0],))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org[0],))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org[0],))
conn.commit()

cur.close()

# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT org, count FROM Counts ORDER BY count'

#for row in cur.execute(sqlstr):
    #print(str(row[0]), row[1])