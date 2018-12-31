import numpy as np
import random
import networkx as nx
from networkx.algorithms import bipartite






def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data


def create_geaph(data, percentage):
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
    print("sa")
    bi0 = list(bi0)
    bi1 = list(bi1)
    random.seed()
    for i in range((int)(percentage / 100 * len(bi0))):
        r = random.randint(1, len(bi0) - 1)
        print(i)
        if bi0[r] not in bi0_sample:
            bi0_sample.append(bi0[r])

    random.seed()
    for i in range((int)(percentage / 100 * len(bi1))):
        r = random.randint(1, len(bi1) - 1)
        print(i)
        if bi1[r] not in bi1_sample:
            bi1_sample.append(bi1[r])
    sample_node = sum([bi0_sample, bi1_sample], [])
    print("salam")
    g = B.subgraph(sample_node)
    return g




data = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/out.actor-movie')
g=create_geaph(data,20)
a=bipartite.average_clustering(g)
print(a)
