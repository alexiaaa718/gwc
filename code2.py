#Graph code 2

from igraph import * #importing igraph library

g = Graph(3) #3 nodes

g.add_edge(0,1)
g.add_edge(1,2)

for i in range(0, g.vcount()): #g.count() coounts the number of nodes 
print(g.degree(i) 