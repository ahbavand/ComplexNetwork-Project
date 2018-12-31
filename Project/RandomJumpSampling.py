import numpy as np
import random
import networkx as nx
from networkx.algorithms import bipartite
import random


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

def sampling(g,percentage,p,data):

    sample_node={'a1'}

    selected_node='a1'
    b=True
    while(b):
        if(len(sample_node)>=(int)(percentage/100*514000)):
            b=False

        random_number=random.uniform(0, 1)
        if(random_number<p):
            print(len(sample_node))

            l=len(list(g.neighbors(selected_node)))
            r=random.randint(0,l-1)
            y=list(g.neighbors(selected_node))
            selected_node=y[r]
            sample_node.add(selected_node)

        else:
            l=len(g.nodes)
            r=random.randint(0,l-1)
            y=list(g.nodes)
            selected_node=y[r]
            sample_node.add(selected_node)


    sample_graph=g.subgraph(sample_node)
    return sample_graph


data = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/out.actor-movie')

g=create_geaph(data)

b=sampling(g,20,.9,data)
a=bipartite.average_clustering(b)
print(a)

















