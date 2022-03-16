f1=open("file_Handling/Guido.jpg","rb")
data = f1.read()
print(data)
f2=open("file_Handling/Udemy_Grudo.jpg","wb")

f2.write(data)
print("File written Successfully")
f1.close()
f2.close()