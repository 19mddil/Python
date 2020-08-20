fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("No file with such name")
    quit()
email_con = dict()
for line in fh:
    if not line.startswith('From '): continue
    tmp = line.split()[5];
    email_con[tmp.split(':')[0]] = email_con.get(tmp.split(':')[0],0) + 1
for k,v in sorted([(k,v) for k,v in email_con.items()]):
    print(k,v)
