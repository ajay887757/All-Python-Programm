#n='a4k3b2'
n=input("Enter String with required assumption:")

output=""
for ch in n:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        d=int(ch)
        new=chr(ord(x)+d)
        output=output+new
print(output)
