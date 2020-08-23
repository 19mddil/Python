import json
input = '''[
"id","x","year"
]'''

info = json.loads(input) #info type is list
print(type(info))
print(type(info[0]))
