class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("My Name Is ",self.name)
        print("My Roll No is ",self.rollno)
        print("My Marks Is ",self.marks)

    print(id("self"))

s1=Student("Ajay",103,45)
s1.talk()
    
print(id(s1))
