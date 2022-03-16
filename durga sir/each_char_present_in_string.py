s='ABBACBA'
output=''
for ch in s:
    if ch not in output:
        output=output+ch
for i in output:
    x=s.count(i)
    print("chracter {} present in string={}".format(i,x))
    
