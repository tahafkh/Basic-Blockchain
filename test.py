from Blockchain import Blockchain

bc = Blockchain()
for i in range(1, 10000):
    bc.makeNewBlock(i)

bc.chain[777].transactions = [{
    'sender' : 'sina' ,
    'reciever' : 'taha' ,
    'amount' : '5 BTC'
}
]

print(bc.validate())