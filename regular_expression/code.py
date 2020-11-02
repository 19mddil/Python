"""
    ^ means the beginning of the file
    $ means the end of the file
    . means matches any character except new line
    \d for digits
    \s means matches white space
    \S means matches any non-white space character
    * Repeats a character zero or more times(*? non-greedy)
    + Repeats a character one or more times(+? non-greedy)
    [aeiou] Matches a single character in the listed set
    [^XYZ] Matches a single character not in the listed set
    [a-z0-9] The set of characters can include a range
    (  indicates where string extraction is to start
    )  indicates where string extraction is to end
"""
import re

hand = open('mbox-short.txt')
#print(hand)
for line in hand:
    line = line.rstrip()
    if re.search('^From: ',line):#if line.startswith('From'):
        print(line)
        continue
    if re.search('From: ',line): # if line.find('From: ') >= 0:
        print(line)
#hand.close()
hand = open('mbox-short.txt') #problem why I have to do it 2nd time.
print("================================")
for line in hand:
    line = line.rstrip()
    if re.search('^X\S+:',line):# . means one character,.* means one or more character,\S means single not whitespace character,\S+ means one or more not whitespace character.
        print(line)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
hand = open('mbox-short.txt')
long_string = hand.read()
#print(long_string)
long_list = re.findall('[\s^ ]X\S+:',long_string)
for x in long_list:
    x = x.lstrip();
    print(x)
user_ip_list = re.findall('\S+?@\S+?',long_string)
for x in user_ip_list:
    x = x.strip()
    print(x)
