s=input("Enter Any List only number:")
l=s.split()
i=0
while i<len(l):
    print("The Element presentat +ve index={} and at -ve index={} is {}" .format(i,i-len(l),l[i]))
    i=i+1      
