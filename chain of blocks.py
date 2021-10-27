import hashlib

class MaitCoin:

    def __init__(self,previous_hash,transaction):
        self.previous_hash = previous_hash #storing previous hash
        self.transaction = transaction # taking in the transaction 
        self.data = transaction + "-" + previous_hash # the data
        self.block_hash = hashlib.sha256(self.data.encode()).hexdigest() # using built-in SHA256 in Hexadecimal (optional) to get a new hash

if __name__ == "__main__":
    t = ["Traveller gives 1 MC to Ajax","Lumine recieves 10 MC from Kaeya","Jean gives 10 MC to Diluc","Venti recieves 50 MC from Athear"]
    Chain_of_Blocks = list()
    Chain_of_Blocks.append( MaitCoin("000000",t[0]) )
    for i in range(1,len(t)):
        Chain_of_Blocks.append( MaitCoin(Chain_of_Blocks[i-1].block_hash,t[i]))
    
    for i in Chain_of_Blocks:
        print(i.data,i.block_hash,sep='\n')
