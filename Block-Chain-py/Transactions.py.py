import time
from datetime import datetime

class Transaction:
    def __init__(self,sender,receiver,amount):
        amount = float(amount)
       # print(type(amount))
       # print(amount < 0.0)
        if amount < 0.0:
            self.sender = receiver
            self.receiver = sender
            self.amount = -amount
        else:
            self.sender = sender
            self.receiver = receiver
            self.amount = amount
        self.index = 0
        self.data = str(self.sender) + " -> " +str(self.amount) + " -> " + str(self.receiver) 
        self.date = datetime.now()
    
    def __str__(self):
        return "The transaction of ***" + self.data + "*** took place on " + str(self.date);

if __name__ == "__main__":
    t1 = Transaction("ABC","XYZ",10.5)
    test = t1.__str__()
    print(test)
    t2 = Transaction("ABC1","XYZ1",-10.5)
    test = t2.__str__()
    print(test)