# Update
2020.04.21
- All node/containers have own fixed ip. The information is in the containerip.txt file
- Even indirectly connected nodes share validated transactions in unconfirmed_transaction proprety.
- New blockchian class property, unvalidated_transaction stores transactions that don't pass the validation check.
- After mined in unspecified node, transactions in mined block will be removed in unconfirmed_transaction property in all nodes.
- New method, **tx_validation**, transaction validation function will validate transaction.
ex) Transaction has three items, 'sender', 'receiver', 'amount'.
validation condition : If the amount sum of transactions in unvalidated_transaction is over 100, transactions will be validated and transferred to unconfirmed_transaction. This function return hash list of validated transactions. 
```python
def tx_validation(self):
  summation = 0
  validated_tx_list =[]
  for tx_key,tx_value in list(self.unvalidated_transactions.items()):
      validated_tx_list.append(tx_key)
      summation += float(tx_value[u'amount'])
      if summation >100:                                    
          return True, validated_tx_list

  return False, None
```

- In webapp transaction page, Chain list, pending transaction(Transaction waiting to be mined), unvalidated transaction(Transaction to be validated) are presented


2020.04.18
- Change node connecting system from host and clinet to peer to peer.
- Implement function to connect two node in web app

- Modify add_transaction function with announce new transaction to peers

## Need to be
- Attach comment and explanation in all API and method in code.

# Purpose
Try to modify below code
- transaction validation update

---

# python_blockchain_app

A simple tutorial for developing a blockchain application from scratch in Python.

## What is blockchain? How it is implemented? And how it works?

Please read the [step-by-step implementation tutorial](https://www.ibm.com/developerworks/cloud/library/cl-develop-blockchain-app-in-python/index.html) to get your answers :)

## Instructions to run

Clone the project,

```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
```

Install the dependencies,

```sh
$ cd python_blockchain_app
$ pip install -r requirements.txt
```

Start a blockchain node server,

```sh
# Windows users can follow this: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=node_server.py
$ flask run --port 8000
```

One instance of our blockchain node is now up and running at port 8000.


Run the application on a different terminal session,

```sh
$ python run_app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).

Here are a few screenshots

1. Posting some content

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/1.png)

2. Requesting the node to mine

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/2.png)

3. Resyncing with the chain for updated data

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/3.png)

To play around by spinning off multiple custom nodes, use the `register_with/` endpoint to register a new node. 

Here's a sample scenario that you might wanna try,

```sh
# Make sure you set the FLASK_APP environment variable to node_server.py before running these nodes
# already running
$ flask run --port 8000 &
# spinning up new nodes
$ flask run --port 8001 &
$ flask run --port 8002 &
```

You can use the following cURL requests to register the nodes at port `8001` and `8002` with the already running `8000`.

```sh
curl -X POST \
  http://127.0.0.1:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

```sh
curl -X POST \
  http://127.0.0.1:8002/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

This will make the node at port 8000 aware of the nodes at port 8001 and 8002, and make the newer nodes sync the chain with the node 8000, so that they are able to actively participate in the mining process post registration.

To update the node with which the frontend application syncs (default is localhost port 8000), change `CONNECTED_NODE_ADDRESS` field in the [views.py](/app/views.py) file.

Once you do all this, you can run the application, create transactions (post messages via the web inteface), and once you mine the transactions, all the nodes in the network will update the chain. The chain of the nodes can also be inspected by inovking `/chain` endpoint using cURL.

```sh
$ curl -X GET http://localhost:8001/chain
$ curl -X GET http://localhost:8002/chain
```
