import imp


import jsonpickle

class Empolyee:
    def __init__(self,eno,ename,esal,eaddr,isMarried):
        self.eno=eno,
        self.ename=ename,
        self.esal=esal,
        self.eaddr=eaddr
        self.isMarried=isMarried

    def display(self):
        print("Eno :{} ,Ename :{}, Esal :{} ,Eaddr :{} ,IsMarried :{}".format(self.eno,self.ename
        ,self.esal,self.eaddr,self.isMarried))

e=Empolyee(101,"Ajay","1000.0","Hydrabad",True)

json_string=jsonpickle.encode(e)
print(json_string)
with open("json_programm/Customize_object/emp11.json","w") as f:
    f.write(json_string)

ee=jsonpickle.decode(json_string)
print(type(ee))
print(ee)
ee.display()

with open("json_programm/Customize_object/emp11.json","r")as f:
    json_string=f.readline()

et=jsonpickle.decode(json_string)

et.display()