import json
# Deserialization json string to python dict

# json_string="""{
# "name":"Ajay",
# "age":19,
# "salary":1000.0,
# "isMarried":true,
# "is_HavingGF":null

# }"""

# employee=json.loads(e)
# print(employee)

# Deserialization json file to python dict

with open("json_programm\json1.json1.json","r") as f:
    employee=json.load(f)


print(employee)