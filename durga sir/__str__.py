class Student:
    def __init__(self,name,rollmo,marks):
        self.name=name
        self.rollno=rollmo
        self.marks=marks

    def __str__(self) :
        return self.name

s1=Student("Ajay",5,67)
s2=Student("Sunny",73,96)
s3=Student("Deepak",10,57)

# print(s1)  <__main__.Student object at 0x00000285E5985130>
# print(s2)  <__main__.Student object at 0x00000285E59851F0>
# print(s3)   <__main__.Student object at 0x00000285E5985EB0>

print("After defing __str__")

print(s1)
print(s2)  
print(s3)

