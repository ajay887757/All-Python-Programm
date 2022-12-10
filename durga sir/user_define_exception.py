class TooYoung(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOld(Exception):
    def __init__(self,msg):
        self.msg=msg

x=int(input("Enter Age"))

if x<18:
    raise TooYoung("Please wait some more time")
elif x>80:
    raise TooOld("Your Age limit is expire so i cannt help you ")
else:
    print("Your Are eligible for marriege ")

