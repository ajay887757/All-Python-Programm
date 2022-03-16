import json

employee={
    "Name":"Ajay",
    "Age":19,
    "Salary":25000,
    "ismarried":True,
    "isHavingGF":None

}
# seralization dict to json string

json_string=json.dumps(employee,indent=4,sort_keys=True)
print(json_string)


#seralization dict to json file

with open("json_programm\json1.json","w") as f:
    json.dump(employee, f)
print("Data writing Successfully")
