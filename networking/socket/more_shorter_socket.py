import urllib.request,urllib.parse,urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    #print(type(line))
    #print(type(line.decode()))
    print(line.decode().strip()) #Actually we are converting byte
