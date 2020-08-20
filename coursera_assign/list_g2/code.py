fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("No file with such name")
    quit()
count = 0
lemails = list()
for line in fh:
    if not line.startswith('From '): continue
    lemails.append(line.split()[1])
    count += 1
for email in lemails:
    print(email)
print("There were", count, "lines in the file with From as the first word")
