vowels=['a','e','i','o','u']
s=input("Enter any string")
result=[]

result=[ch for ch in vowels if ch in s]
print(result)
print("The Number of unique vowels ",len(result))
