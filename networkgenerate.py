import networkx 
import matplotlib.pyplot as plt
import math
import yaml
'''
Erdős–Rényi model
n is number of nodes
Almost every graph in G(n, 2ln(n)/n) is connected.
As n tends to infinity, the probability that a graph on n vertices with edge probability 2ln(n)/n is connected, tends to 1.
https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
'''

n = 20
p = 2*math.log(n)/n

graphconnected=True

while graphconnected:
    graph = networkx.generators.random_graphs.erdos_renyi_graph(n,p)
    if networkx.is_connected(graph) == True:
        graphconnected = False




with open('./docker-compose.yml') as ymlfile:
    data = yaml.load(ymlfile)

nodetemplate =  {'node2': 
                    {'image': 'pythonblockchainapp_node1', 
                    'ports': ['8002:5000'], 
                    'command': ['python', 'node_server.py'], 
                    'networks': {'testing_net': {'ipv4_address': '172.28.1.2'}}}}


for nodeindex in range(1,n+1):
    nodename = 'node'+str(nodeindex)
    port = str(8000+nodeindex)+':5000'
    ipaddress = '172.28.1.%s'%(nodeindex)
    node = {nodename: 
                    {'image': 'pythonblockchainapp_node1', 
                    'ports': [port], 
                    'command': ['python', 'node_server.py'], 
                    'networks': {'testing_net': {'ipv4_address': ipaddress}}}}
    
    data['services'][nodename] = node[nodename]



with open('./docker-composev2.yml' ,'w') as ymlfile:
    yaml.dump(data,ymlfile,default_flow_style=False)


edgelist = list(graph.edges())

for pos,(fn,tn) in enumerate(edgelist):   
    edgelist[pos] = (fn+1,tn+1)

connectionlist=[]
for fn,tn in edgelist:
    fnip = 'http://172.28.1.'+str(fn)+':5000/register_with'
    tnip = 'http://172.28.1.'+str(tn)+':5000'
    connectionlist.append((fnip,tnip))


with open('./testscript.sh','w') as f:
    f.write('#!/bin/sh\n')
    f.write('\n')
    for fnip,tnip in connectionlist:
        request = "curl -X POST "+fnip+" -H 'Content-Type: application/json' -d '{\"node_address\": \""+tnip+"\"}'\n"
        f.write(request)
f.close()

fig = plt.figure(3,figsize=(20,20))
ax= fig.subplots()

networkx.draw(graph,with_labels=True)

ax.set_title('Network Structure',fontsize=20)
# plt.show()
plt.savefig('./networkstructure.png',bbox_inches = "tight")