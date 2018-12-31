import numpy as np
import random
import networkx as nx
from networkx.algorithms import bipartite
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics.ThresholdModel as th
import operator
from collections import OrderedDict
from operator import itemgetter



def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data



def create_geaph(data,percentage):
    a = len(data)
    li = []
    for i in range(0, (int)(len(data)*percentage/100)):
        li.append(i)
    bi0 = {'a1'}
    bi1 = {'b1'}
    edges = []
    bi0_sample = []
    bi1_sample = []
    for i in range(0, len(li)):
        e = 'a' + (str)((int)(data[li[i]][0]))
        #    print(e)
        w = 'b' + (str)((int)(data[li[i]][1]))
        edges.append((e, w))
        bi0.add(e)
        bi1.add(w)
    B = nx.Graph()
    B.add_nodes_from(bi0, bipartite=0)
    B.add_nodes_from(bi1, bipartite=1)
    B.add_edges_from(edges)
    return B



data = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/out.actor-movie')
g=create_geaph(data,10)
a=list(g.degree())
sorted_degree=(sorted(a,key=lambda l:l[1],reverse=True))
# Model selection
model = th.ThresholdModel(g)

# Model Configuration
config = mc.Configuration()
config.add_model_parameter('percentage_infected', 0.01)

# Setting node parameters
threshold = 4/10
for i in g.nodes():
    config.add_node_configuration("threshold", i, threshold)

seed=[]
for i in range(0,10000):
    seed.append(sorted_degree[i][0])
#print(seed)
#print(sorted_degree)

config.add_model_initial_configuration("Infected",seed)
model.set_initial_status(config)

# Simulation execution
iterations = model.iteration_bunch(200)
print(iterations)
print(iterations[199])
