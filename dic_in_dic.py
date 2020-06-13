users ={
    'x' : {
        'first':'karim',
        'last' : 'Rahman',
        'location' : 'Dhaka'
    },
    'y':{
        'first':'Rahim',
        'last':'Islam',
        'location':'Naogaon'
    }
}
for tag in users.keys():
    print(tag+" : ")
    for key in users[tag]:
          print("\t"+key+ " : "+users[tag][key])  

users ={
    'x' : {
        'first':'karim',
        'last' : 'Rahman',
        'location' : 'Dhaka'
    },
    'y':{
        'first':'Rahim',
        'last':'Islam',
        'location':'Naogaon'
    }
}
for tag,info in users.items():
    print(tag+" : ")
    for key in info.keys():
          print("\t"+key+ " : "+users[tag][key])  

users ={
    'x' : {
        'first':'karim',
        'last' : 'Rahman',
        'location' : 'Dhaka'
    },
    'y':{
        'first':'Rahim',
        'last':'Islam',
        'location':'Naogaon'
    }
}
for tag,info in users.items():
    print(tag+" : ")
    for key,value in info.items():
          print("\t"+key+ " : "+value)  
