class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,others):
        return self.marks>others.marks
    def __ge__(self,others):
        return self.marks>=others.marks
    
s1=Student("Ajay", 75)
s2=Student("Ravi", 90)
s3=Student("Sunny",56)
print(s1>s2)
print(s1<s2)
print(s3<s2)
print(s1>=s3)
print(s1<=s3)
