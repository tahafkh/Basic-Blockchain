import hashlib
import time

class Block:

    def __init__(self, proof, index, previousHash, transactions):
        self.index = index
        self.proof = proof
        self.previousHash = previousHash
        self.transactions = transactions
        self.timestamp = time.time()
    
    @property
    def hash(self):
        rawString = "{}{}{}{}{}".format(self.index, self.proof, self.previousHash, self.transactions, self.timestamp)
        return hashlib.sha256(rawString.encode()).hexdigest()
    
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.makeGenesis()
    
    def makeGenesis(self):
        self.makeNewBlock(proof = 0)

    def makeNewBlock(self, proof):
        if(len(self.chain)):
            newBlock = Block(proof, len(self.chain), self.lastBlock.hash, self.pendingTransactions)
        else:
            newBlock = Block(proof, len(self.chain), 0, self.pendingTransactions)
        self.pendingTransactions = []
        self.chain.append(newBlock)
        return newBlock

    def validate(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if (current.index != previous.index + 1):
                return "It's been changed"
            if (previous.timestamp > current.timestamp):
                return "It's been changed"
            if (current.previousHash != previous.hash):
                return "It's been changed"
        return "It hasn't been changed"

    def makeNewTransaction(self, sender, reciever, amount):
        self.pendingTransactions.append(
            {
                'sender' : sender,
                'reciever' : reciever,
                'amount' : amount
            }
        )
        return True
    
    @property
    def lastBlock(self):
        return self.chain[-1]