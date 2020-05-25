import pymongo
from pymongo import MongoClient
import eventgenerator
import time
import json
import requests
from bson.json_util import dumps


conn = MongoClient('127.0.0.1:27017')
# conn.drop_database('blockchaindb')
db = conn.blockchaindb

collect = db.transactions

e_time = 3
count = 0
start_time = time.time()
while True:
    now = time.time()
    if now > start_time +e_time:
        break
    nt,node = next(eventgenerator.newevent(3))
    port = 8000+node
    CONNECTED_NODE_ADDRESS = 'http://127.0.0.1:'+str(port)+'/'

    sender = nt["sender"]
    receiver = nt["receiver"]
    amount = nt["amount"]
    correlational_identifier = nt['CI']

    post_object = {
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    }

    # # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                    json=post_object,
                    headers={'Content-type': 'application/json'})


# cursor = collect.find({},{'_id':0})
# documents = []
# with open('./output.json','wb') as f:
#     for document in list(cursor):
#         documents.append(document)
#     json.dump(documents,f)