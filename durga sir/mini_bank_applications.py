class Customer:
    """Welcome to The Bank OF Ajay"""
    bankname="Ajay Bank"

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdrow(self,amount):
        if amount>self.balance:
            print("Insifficent Found ")
        else:
            self.balance=self.balance-amount

        

print("Welcome to ",Customer.bankname)

name=input("Enter Your Name: ")

c=Customer(name)

while True:
    print("*"*40)
    print("Chose One Optons")
    print("*"*40)
    print("d   -  Deposit\nw  -  withdrow\ne   -  exit\nb   -  Check Balance")
    options=input("Choose One")
    if options.lower()=='d':
        amount=float(input("Enter Deposit Amount"))
        c.deposit(amount)
        print("Now Avialable Blance :",c.balance)
    elif options.lower()=='w':
        amount=float(input("Enter Withdrow Amount"))
        c.withdrow(amount)
        print("Now Avialable Blance :",c.balance)
    elif options.lower()=='e':
        print("Thanks For Using Our Bank")
        break
    elif options.lower() =="b":
        print("Available balance :", c.balance)
    else:
        print("Choose correct option")
        
