s=input("Enter Digits and character:")
alphabet=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        digit.append(ch)
print("".join(sorted(alphabet)+sorted(digit)))
