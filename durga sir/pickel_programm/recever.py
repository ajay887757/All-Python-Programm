import pickle
with open("pickel_programm/emp.ser","rb") as f:
    while True:
        try:
            new_obj=pickle.load(f)
            new_obj.display()
        except EOFError:
            print("Deserialization Completed")
            break
        


