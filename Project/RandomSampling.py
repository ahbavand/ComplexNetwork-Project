import numpy as np
import igraph as ig
from scipy import spatial
from scipy import linalg as LA
from sklearn.cluster import KMeans
import random
import networkx as nx
from networkx.algorithms import bipartite

def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data


def create_graph(data):
    bi0 = {'a1'}
    bi1 = {'b1'}
    edges=[]


    for i in range(0,int(len(data)/1)):

        e='a'+(str)((int)(data[i][0]))
        w='b'+(str)((int)(data[i][1]))
       # print(e)
       # print(w)
        edges.append((e,w))


        bi0.add(e)
        bi1.add(w)
        print(len(bi0))


       # bi0.add( int(data[i][0]))
       # bi1.add(data[i][1])
       # edges.append((int(data[i][0]),data[i][1]))

   # print(bi1)
   # print(bi0)

    B = nx.Graph()
    B.add_nodes_from(bi0, bipartite=0)
    B.add_nodes_from(bi1, bipartite=1)
    print("sa")
    B.add_edges_from(edges)
    print("sa")
    return B





data = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/out.actor-movie')
B=create_graph(data)
print("Sa")
#print(nx.algorithms.distance_measures.diameter(B))
print(nx.number_connected_components(B))


  #  e = (data[:,0], bipartite=0)
  #  w = (data[:,1])



