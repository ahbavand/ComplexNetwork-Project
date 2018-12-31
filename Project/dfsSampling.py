import numpy as np
import random
import networkx as nx
from networkx.algorithms import bipartite



def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data

def create_geaph(data):
    a = len(data)
    li = []
    for i in range(0, len(data)):
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
    print("sa")
    B.add_edges_from(edges)
    return B



def sampling(g,percentage,data):
    edges=(list(nx.dfs_edges(g,'a1'))[0:(int)(percentage/100*len(data))])
    B = nx.Graph()
    B.add_edges_from(edges)
    return B


data = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/out.actor-movie')
g=create_geaph(data)
e=sampling(g,20,data)
a=bipartite.average_clustering(e)
print(a)

