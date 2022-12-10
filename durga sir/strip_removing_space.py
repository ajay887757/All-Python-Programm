city=input("Enter Your City Name:").strip()
#scity=city.strip()
#lstrip() removing space from beging
#rstrip()removing space from end
#strip()removing space from both side
if city=="Hydrabad":
    print("Hello Hydrabadi ......aslam alkum")
elif city=="Darbhanga":
    print("Hello Darbhangiya Ram Ram")
elif city=='Delhi':
    print("Hello {}".format(city))
else:
    print("you enter worng city")
    
