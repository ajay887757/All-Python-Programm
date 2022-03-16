n=input("Enter Any string")
a="abcdefghijkl"
print("s" in a)
print("j" not in a)
print("Aj" in "Ajay")
print("="*len(n))
for i in n:
    print(i in a)
    print(i not in a)

