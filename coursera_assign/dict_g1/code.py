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
    email_con[line.split()[1]] = email_con.get(line.split()[1],0) + 1
max_key = None
max_value = None
for k,v in email_con.items():
    if max_value is None or v > max_value:
        max_value = v
        max_key = k

print(max_key,max_value)
