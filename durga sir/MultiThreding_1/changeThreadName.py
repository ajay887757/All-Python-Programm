from threading import *

print("Current Ttread Name :",current_thread().getName())
current_thread().setName("Ajay Thread")
# print("Current Ttread Name :",current_thread().name)
print("Current Ttread Name :",current_thread().getName())