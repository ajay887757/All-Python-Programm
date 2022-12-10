s=eval(input("Enter Any Set"))
n=int(input("Enter Element you want to delete"))
if n in s:
    #s.remove(n)
    s.discard(n)
    print("Delete Successfully")
    print(s)
else:
    print("Enter valid deleting element")

print("Lenght of element is",len(s))
    
