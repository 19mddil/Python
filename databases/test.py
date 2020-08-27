import re

orgs = list()
fh = open('mbox.txt')
for line in fh:
	if not line.startswith('From: '):continue
	pieces = line.split()
	email = pieces[1]
	org = re.findall('@(.+)',email)
	orgs.append(org[0])
for k in set(orgs): print(k)
