import numpy as np
import math  
import time
import pandas as pd

import sys
sys.path.insert(0,'../python_blockchainapp/')
import quality_control


class create_event:
    def __init__(self):
        self.ci_candidates = [x+1 for x in range(9)]
        self.used_ci_candidates = {}

    def newevent(self,node_number):
        node = np.random.choice(node_number,1)  
        datatype_choice = np.random.rand(1)

        ci = int(np.random.choice(self.ci_candidates,1)[0])
        if ci not in self.used_ci_candidates.keys():
            term = 1
            self.used_ci_candidates[ci]={term:set()}
        else:
            term = sorted(self.used_ci_candidates[ci].keys())[-1]
            if 1 in self.used_ci_candidates[ci][term] and 2 in self.used_ci_candidates[ci][term]:
                term +=1
                self.used_ci_candidates[ci][term]=set()
            elif 1 in self.used_ci_candidates[ci][term] and 2 not in self.used_ci_candidates[ci][term]:
                datatype_choice = 0
            elif 1 not in self.used_ci_candidates[ci][term] and 2 in self.used_ci_candidates[ci][term]:
                datatype_choice = 1


        d1 =int(math.ceil(np.random.exponential(scale=10,size=1)[0]))
        d2 =int(math.ceil(np.random.exponential(scale=10,size=1)[0]))
        
        if  datatype_choice>0.5:
            datatype=1
            transaction = {'ci':ci,'data':{'d1':d1}}
        else:
            datatype=2
            transaction = {'ci':ci,'data':{'d2':d2}}
        
        self.used_ci_candidates[ci][term].add(datatype)
        return (transaction,term,node[0]+1)

    def invoke_event(self,e_time,node_number):
        
        start_time = time.time()
        while True:
            now = time.time()
            if now > start_time +e_time:
                break
            return self.newevent(node_number)
            


if __name__ =='__main__':
    qc_checker = {}
    generator = generate_event()
    for x in range(50):
        t = generator.newevent(3)
        qc_id = '%s_%s'%(t[0]['ci'],str(t[1]))        
        if qc_id not in qc_checker:
            qc_checker[qc_id] = quality_control.QualityControl(CI=t[0]['ci'],term=t[1])
        if bool('d1' in t[0]['data']):
            qc_checker[qc_id].add_variable('d1',t[0]['data']['d1'])
        else:
            qc_checker[qc_id].add_variable('d2',t[0]['data']['d2'])
        print(qc_checker[qc_id].tx_content())
        