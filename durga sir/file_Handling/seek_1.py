f=open("file_Handling/file.txt","r+")
print(f.read())
print("Current Possion of The curser is",f.tell())
f.seek(18)
f.write("Good!!!")
print("Current Possion of The curser is",f.tell())
f.seek(0)
print("After Updation")
print(f.read())
f.close()