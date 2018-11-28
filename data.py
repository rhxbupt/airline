import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv("559550570_T_T100D_MARKET_US_CARRIER_ONLY 4.csv")
print('total length: ', len(data))
# index=["one","two","three","four"]

origin = data['ORIGIN']
destination = data['DEST']
distance = data['DISTANCE']


df = pd.DataFrame(data, columns = ['a','b','c','d','e','f','g','h','i'])


# we can set alpha, beta, gama... as different parameters and multiply them 
# to "passengers, distance ... "to generate a metric to represent the edge weight
print('graph: ')
# graph related
g = nx.Graph()
for i in range(len(origin)):
	# g.add_edge(origin[i], destination[i])
	g.add_weighted_edges_from([(origin[i], destination[i], distance[i])])

# 遍历图里每个edge
# for n, nbrs in g.adj.items():
# 	for nbr, eattr in nbrs.items():
# 		wt = eattr['weight']
# 		if wt > 6500: print('(%s, %s, %d)' % (n,nbr,wt))

#information about the graph
# print(nx.info(g))

# print(g.degree('LAX'))
# print(list(g.adj['LAX']))

#draw the whole graph
# nx.draw(g, with_labels = True)

# graph for LA
gLA = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'LAX' ):
		gLA.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gLA.add_edge(origin[i], destination[i])

# graph for ATL
gATL = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'ATL'):
		gATL.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gATL.add_edge(origin[i], destination[i])

# graph for CLT
gCLT = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'CLT'):
		gCLT.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gCLT.add_edge(origin[i], destination[i])

# graph for ORD
gORD = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'ORD'):
		gORD.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gORD.add_edge(origin[i], destination[i])

# graph for DAL
gDAL = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'DAL' ):
		gDAL.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gDAL.add_edge(origin[i], destination[i])

# graph for DEN
gDEN = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'DEN'):
		gDEN.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gDEN.add_edge(origin[i], destination[i])

# graph for JFK
gJFK = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'JFK'):
		gJFK.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gJFK.add_edge(origin[i], destination[i])

# graph for LAS
gLAS = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'LAS'):
		gLAS.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gLAS.add_edge(origin[i], destination[i])

# graph for SFO
gSFO = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'SFO'):
		gSFO.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gSFO.add_edge(origin[i], destination[i])

# graph for SEA
gSEA = nx.Graph()
for i in range(len(origin)):
	if(origin[i] == 'SEA'):
		gSEA.add_weighted_edges_from([(origin[i], destination[i], distance[i])])
		# gSEA.add_edge(origin[i], destination[i])

print(gLA.degree('LAX'))

print(len(data[data.ORIGIN == 'LAX']) )
print(nx.info(gLA))

options = {
	'node_size' : 10,
	'width' : 0.5,
}
nx.draw(gLA, with_labels = True, **options)

plt.show()