import json

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
# e_dict={'eno':e.eno,"ename":e.ename,"esal":e.esal,"eaddr":e.eaddr}
# print(e_dict)
e_dict=e.__dict__
print(e_dict)


# Serialization python dict to json string

json_string=json.dumps(e_dict)
print(json_string)

#Serialization Python Dict to json file

with open("json_programm/Customize_object/emp.json","w") as f:
    json.dump(e_dict,f)


# Deserialization Json String to python object

e_new_dict=json.loads(json_string)

e=Empolyee(e_new_dict["eno"],e_new_dict["ename"],e_new_dict["esal"],e_new_dict["eaddr"],e_new_dict["isMarried"])

e.display()

