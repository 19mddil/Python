phrase = "Don't panic!"
plist = list(phrase)#turing string into list
print(phrase)
print(plist)
for i in range(4):
	plist.pop()
#Don't pa
new_phrase = "".join(plist[1:3])
print(new_phrase)
new_phrase = new_phrase+"".join([plist[5],plist[4]])
print(new_phrase)
new_phrase = new_phrase+"".join(plist[7:5:-1])
print(plist)
print(new_phrase)