cost=eval(input("Enter Data in list: "))
for iteam in cost:
    if iteam>500:
        print("To Place this order insurece must be required")
        break
    print("processing item ",iteam,cost.index(iteam))
