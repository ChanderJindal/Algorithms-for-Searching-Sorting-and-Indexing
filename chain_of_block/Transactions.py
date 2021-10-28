import time
from datetime import datetime

class Transaction:
    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.data = str(sender) + " -> " +str(amount) + " -> " + str(receiver) 
        self.date = datetime.now()
    
    def printer(self):
        print("The transaction of ",self.data," took place on",self.date )

if __name__ == "__main__":
    t1 = Transaction("ABC","XYZ",10.5)
    t1.printer()


        