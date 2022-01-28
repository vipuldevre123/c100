class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        

    def checkbalance(self):
        print("your balance is 50,000")

    def withdrawl(self,amount):
        newbalance=50000-amount
        print("your remaining balance is",newbalance)   

    

#class object
cardnumber=input("Enter Your Card Number")
pin=input("Enter Your Pin")
o=Atm(cardnumber,pin)

o.checkbalance()
o.withdrawl(1000)