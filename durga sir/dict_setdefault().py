d=eval(input("Enter Dict:"))
key=int(input("Enter Key you want to add"))
value=input("Enter Value ")

#d[key]=value

d.setdefault(key,value)
print(d)
