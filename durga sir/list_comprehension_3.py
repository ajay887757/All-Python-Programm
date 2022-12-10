vowels=['a','e','i','o','u']
s=input("Enter any string")
result=[]
for ch in vowels:
    if ch in s:
        result.append(ch)
print(result)
print("The no of vowel is",len(result))
