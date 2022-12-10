city=input("Enter Your City Name:").strip()
#scity=city.strip()
#lstrip() removing space from beging
#rstrip()removing space from end
#strip()removing space from both side
city=city.lower()
if city=="hydrabad":
    print("Hello Hydrabadi ......aslam alkum")
elif city=="darbhanga":
    print("Hello Darbhangiya Ram Ram")
elif city=='delhi':
    print("Hello {}".format(city))
else:
    print("you enter worng city")
    
