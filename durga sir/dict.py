d={'A':2,'B':3}
  # key :value
d={}
d['A']=100
d["B"]=200
print(d)
d['A']=4000
print(d)
print(d.get('A'))
print(d.get('Z'))
x=d.get('z',0)
print(x)

print("==================================================================")

d={}
d["A"]=1
d["B"]=2
d["A"]=d.get("A",0)+1
print(d)
d["A"]=d.get("Z",0)+1
print(d)

