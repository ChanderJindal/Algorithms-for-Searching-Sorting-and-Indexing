from Transactions import Transaction as T
import hashlib
from datetime import datetime
class Block:
    def __init__(self,prev,t,index) -> None:
        self.prev = prev 
        self.transaction = t
        self.date = datetime.now()
        self.data = str(self.prev) + str(self.transaction.data) + str(self.date)
        self.hash = hashlib.sha256(  self.data.encode() ).hexdigest()
        self.nonse = 0
        self.index = index
    
    def printer(self):
        self.transaction.printer()
        print("The Previous Hash is: ",self.prev,'\n',"The Current Hash is: ", self.hash,'\n',"The ",self.index," Block was gotten on Date: ", self.date,sep="",end="\n\n")
        #print(self.hash)

    def mineBlock(self, difficulty):
        arr = []
        for i in range(0, difficulty):
            arr.append(i)
		
        arrStr = map(str, arr)
        hashPuzzle = ''.join(arrStr)
		#print(len(hashPuzzle));
        while self.hash[0:difficulty] != hashPuzzle:
            self.nonse += 1
            self.hash = self.calculateHash()
			#print(len(hashPuzzle));
			#print(self.hash[0:difficulty]);
        print("Block Mined!")
        return True

if __name__ == "__main__":
    T1 = T("ABC","QWERTY",1.25)
    B1 = Block("None",T1,0)
    B1.printer()