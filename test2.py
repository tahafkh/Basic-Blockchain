from Blockchain import Blockchain

bc = Blockchain()
for i in range(1, 10000):
    bc.makeNewBlock(i)

bc.chain[8000].transactions = [{
    'sender' : 'sina' ,
    'reciever' : 'taha' ,
    'amount' : '5 BTC'
}
]

for i in range(8001, 10000):
    bc.chain[i].previousHash = bc.chain[i-1].hash

print(bc.validate())