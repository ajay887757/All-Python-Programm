n=input("Enter String with required assumption:")
output=""   #aeknbd
i=0
j=1
for ch in n:
    if ch.isalpha():
        x=ord(n[i])+int(n[j])
        y=chr(x)
        output=output+n[i]+y
        i=i+2
        j=j+2
print(output)
        
        
