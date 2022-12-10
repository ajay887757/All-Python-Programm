s='ABCDEFG'
#find()
print(s.find('C'))
print(s.find('H')) #IF H IS NOT FIND THEN IT RETURN -1
print(s.find("C",2,6)) #BOUNDRARY TO FIND INDEX
print(s.find("D",2,len(s)))
print(s.find("E",2))

print("===========================================")

#rfind()
s1='abcba'
print(s1.rfind('b'))
print(s1.rfind('u')) # value is present in s1 then its return -1
print(s1.rfind('b',1,4))

#find(substring,begin,end)      begin to end-1
