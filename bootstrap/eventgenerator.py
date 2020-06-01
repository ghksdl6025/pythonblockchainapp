import numpy as np
import math  
import time
def newevent(node_number):
    node = np.random.choice(node_number,1)
    candidates =['a','b','c','d','e']
    correlational_identifier = ['x1','x2','x3','x4']
    amount = int(math.ceil(np.random.exponential(scale=10,size=1)[0]))
    sender,receiver = np.random.choice(candidates,2,replace=False)
    ci = np.random.choice(correlational_identifier,1)[0]
    transaction = {'sender':sender,'receiver':receiver,'amount':amount,'CI':ci}
    
    yield (transaction,node[0]+1)

def event_generate(e_time):
    count = 0
    start_time = time.time()
    while True:
        now = time.time()
        if now > start_time +e_time:
            break
        yield next(newevent())
        count +=1


if __name__ =='__main__':

    print(len(list(event_generate(5))))