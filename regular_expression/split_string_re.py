import re
grades = "ABAAABBCcACczzCc"
#spliting string by 'CC'
splitted_list = re.findall('(.+?)Cc',grades) #This do not leave a trace
print(splitted_list)
