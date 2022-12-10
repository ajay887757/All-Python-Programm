vowels=['a','e','i','o','u']
s=input("Enter any string")
result=[]
for x in s:
    if x in vowels:
        if x not in result:
            result.append(x)
        
print(result)
print("The Number of unique vowels ",len(result))
