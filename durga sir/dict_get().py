d={100:'A',200:'B',300:'C',400:'D'}
key =int(input("Enter Key"))
if key in d:
    print("Corresponding value",d.get(key))
    #print("Corresponding value",d[key])
    
else:
    print("Key is not avialable", key)
