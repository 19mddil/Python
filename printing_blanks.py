cat = 'MeowMeowCutty'
p = False
for c in cat:
    #if c:
    if p:
        print(' ',end = '')
    p = True;
    print(c,end = '')
