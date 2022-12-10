n=input("Enter charcter and digit") # a4b3c2
s=""
for ch in n:
    if ch.isalpha():
        x=ch
    else:
        s=s+x*int(ch)
        #print(x*int(ch),end="")
print(s)

    
