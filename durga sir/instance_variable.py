class Student:
    def setName(self,namme):
        self.name=name
        
    def getName(self):
        #print("Hi",self.name)
        return self.name
        
    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        #print("Your Marks Are",self.marks)
        return self.marks

    def grade(self):
        if self.marks>=60:
            #print("You Got grade A")
            return "A"
        elif self.marks>=50:
            #print("You Got grade B")
            return "B"

        elif self.marks>=35:
            #print("You Got grade C")
            return "C"

        else:
            #print("You are failed")
            return "You are Failed"


n=int(input("Enter number Of Students"))

list=[]

for i in range(n):
    s=Student()
    name=input("Enter Student Name:")
    marks=int(input("Enter Marks"))

    s.setName(name)
    s.setMarks(marks)
    s.getName()
    s.getMarks()
    #s.grade()
    list.append(s)


for j in list:
    print('Hello',j.getName())
    print("Your Marks are:",j.getMarks())
    print("Your Got Grade:",j.grade())


        
