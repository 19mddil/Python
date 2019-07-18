phrase = "Don't panic!"
plist = list(phrase)#turing string into list
print(phrase)
print(plist)
#ont pa
for i in range(4):
	plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([ plist.pop(3),plist.pop(2),plist.pop(),plist.pop() ] )
new_phrase = "".join(plist)#turning list into string
#you can use a '' too
print(plist)
print(new_phrase)