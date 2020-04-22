import networkx 
import matplotlib.pyplot as plt
import math
'''
Erdős–Rényi model
n is number of nodes
Almost every graph in G(n, 2ln(n)/n) is connected.
As n tends to infinity, the probability that a graph on n vertices with edge probability 2ln(n)/n is connected, tends to 1.
https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
'''

n = 50
p = 2*math.log(n)/n
graph = networkx.generators.random_graphs.erdos_renyi_graph(n,p)

print(p)
# networkx.draw(graph)
# plt.show()

