fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Such file do not exist')
    quit()
lst = list()
for line in fh:
    for word in line.split():
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)
