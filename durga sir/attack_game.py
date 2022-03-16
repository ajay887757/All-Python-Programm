class Game:
    def __init__(self,p1,p2):
        self.life1=5
        self.life2=5
        self.p1=p1
        self.p2=p2
    
    def attack1(self,p1,p2):
        print("Welcome to the Game")
        print("Attack from",p1,"to",p2)
        if self.life1>=1:
            self.life1-=1
        else:
            print("game Over")
    def attack2(self,p1,p2):
        print("Welcome to the Game")
        if self.life2>=1:
            self.life2-=1
        else:
            print("game Over")

    def checklife1(self):
        print(self.life1)
    def checklife2(self):
        print(self.life2)
p1=input("Enter First Player name").lower()
p2=input("Enter Second Player name").lower()
g=Game(p1,p2)
option=input("Enter Player Name you Want to Attack:").lower()
if option==p2:
    g.attack2(p1,p2)
                                                                
else:
    g.attack1(p1,p2)

option2=input("Check life [p1/p2]")
if option2.lower()==p1:
    g.checklife1()
elif option2.lower()==p2:
    g.checklife2()

