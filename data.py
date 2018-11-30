import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv("559550570_T_T100D_MARKET_US_CARRIER_ONLY 4.csv")
# print('total length: ', len(data))
# index=["one","two","three","four"]

origin = data['ORIGIN']
destination = data['DEST']
distance = data['DISTANCE']


df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])


# we can set alpha, beta, gama... as different parameters and multiply them
# to "passengers, distance ... "to generate a metric to represent the edge weight
# print('graph: ')
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

# information about the graph
# print(nx.info(g))

# print(g.degree('LAX'))
# print(list(g.adj['LAX']))

# draw the whole graph
# nx.draw(g, with_labels = True)
graph = nx.Graph()
for i in range(len(origin)):
	graph.add_weighted_edges_from([(origin[i], destination[i], distance[i])])

# graph for LA
gLA = nx.Graph()
for i in range(len(origin)):
    if(origin[i] == 'LAX'):
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
    if(origin[i] == 'DAL'):
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


def draw(str):
	print('***********',str,'***********')

	if(str == "LAX"):
		lax_function()
	if(str == "CLT"):
		clt_function()
	if(str == "ORD"):
		ord_function()
	if(str == "DAL"):
		dal_function()
	if(str == "DEN"):
		den_function()
	if(str == "JFK"):
		jfk_function()
	if(str == "LAS"):
		las_function()
	if(str == "SFO"):
		sfo_function()
	if(str == "SEA"):
		sea_function()				
	if(str == "whole"):
		whole_function()

def whole_function():
	graph_deg_cen = nx.degree_centrality(graph)
	print("The degree centrality of LAX:"+str(graph_deg_cen['LAX']))
	print("The degree centrality of CLT:"+str(graph_deg_cen['CLT']))
	print("The degree centrality of ORD:"+str(graph_deg_cen['ORD']))
	print("The degree centrality of DAL:"+str(graph_deg_cen['DAL']))
	print("The degree centrality of DEN:"+str(graph_deg_cen['DEN']))
	print("The degree centrality of JFK:"+str(graph_deg_cen['JFK']))
	print("The degree centrality of LAS:"+str(graph_deg_cen['LAS']))
	print("The degree centrality of SFO:"+str(graph_deg_cen['SFO']))
	print("The degree centrality of SEA:"+str(graph_deg_cen['SEA']))
	
	LA_clo_cen = nx.closeness_centrality(graph,u='LAX',distance='weight')
	CLT_clo_cen = nx.closeness_centrality(gCLT,u='CLT',distance='weight')
	ORD_clo_cen = nx.closeness_centrality(gORD,u='ORD',distance='weight')
	DAL_clo_cen = nx.closeness_centrality(gDAL,u='DAL',distance='weight')
	DEN_clo_cen = nx.closeness_centrality(gDEN,u='DEN',  distance='weight')
	JFK_clo_cen = nx.closeness_centrality(gJFK, u='JFK', distance='weight')
	LAS_clo_cen = nx.closeness_centrality(gLAS, u='LAS', distance='weight')
	SFO_clo_cen = nx.closeness_centrality(gSFO, u='SFO', distance='weight')
	SEA_clo_cen = nx.closeness_centrality(gSEA, u='SEA', distance='weight')

	print("The closeness centrality of LAX:"+str(LA_clo_cen))
	print("The closeness centrality of CLT:"+str(CLT_clo_cen))
	print("The closeness centrality of ORD:"+str(ORD_clo_cen))
	print("The closeness centrality of DAL:"+str(DAL_clo_cen))
	print("The closeness centrality of DEN:"+str(DEN_clo_cen))
	print("The closeness centrality of JFK:"+str(JFK_clo_cen))
	print("The closeness centrality of LAS:"+str(LAS_clo_cen))
	print("The closeness centrality of SFO:"+str(SFO_clo_cen))
	print("The closeness centrality of SEA:"+str(SEA_clo_cen))



	# print(len(data[data.ORIGIN == 'LAX']))
	print(nx.info(graph))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(graph, with_labels=True, **options)

	plt.show()	

def lax_function():
    print(gLA.degree('LAX'))
    LA_deg_cen = nx.degree_centrality(gLA)
    # print("The degree centrality of LAX:"+str(LA_deg_cen['LAX']))
    print(LA_deg_cen)
    LA_clo_cen = nx.closeness_centrality(gLA, distance='weight')
    # print(LA_clo_cen)
    print("The closeness centrality of LAX:"+str(LA_clo_cen['LAX']))


    print(len(data[data.ORIGIN == 'LAX']))
    print(nx.info(gLA))

    options = {
        'node_size': 10,
        'width': 0.5,
    }
    nx.draw(gLA, with_labels=True, **options)

    plt.show()


def clt_function():
	print(gCLT.degree('CLT'))
	CLT_deg_cen = nx.degree_centrality(gCLT)
	print("The degree centrality of CLT:"+str(CLT_deg_cen['CLT']))
	CLT_clo_cen = nx.closeness_centrality(gCLT, distance='weight')
    
	print("The closeness centrality of CLT:"+str(CLT_clo_cen['CLT']))

	print(len(data[data.ORIGIN == 'CLT']))
	print(nx.info(gCLT))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gCLT, with_labels=True, **options)
	plt.show()





def ord_function():
	print(gORD.degree('ORD'))
	ORD_deg_cen = nx.degree_centrality(gORD)
	print("The degree centrality of ORD:"+str(ORD_deg_cen['ORD']))
	ORD_clo_cen = nx.closeness_centrality(gORD, distance='weight')
    
	print("The closeness centrality of ORD:"+str(ORD_clo_cen['ORD']))

	print(len(data[data.ORIGIN == 'ORD']))
	print(nx.info(gORD))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gORD, with_labels=True, **options)
	plt.show()





def dal_function():
	print(gDAL.degree('DAL'))
	DAL_deg_cen = nx.degree_centrality(gDAL)
	print("The degree centrality of DAL:"+str(DAL_deg_cen['DAL']))
	DAL_clo_cen = nx.closeness_centrality(gDAL, distance='weight')
    
	print("The closeness centrality of DAL:"+str(DAL_clo_cen['DAL']))

	print(len(data[data.ORIGIN == 'DAL']))
	print(nx.info(gDAL))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gDAL, with_labels=True, **options)
	plt.show()




def den_function():
	print(gDEN.degree('DEN'))
	DEN_deg_cen = nx.degree_centrality(gDEN)
	print("The degree centrality of DEN:"+str(DEN_deg_cen['DEN']))
	DEN_clo_cen = nx.closeness_centrality(gDEN, distance='weight')
    
	print("The closeness centrality of DEN:"+str(DEN_clo_cen['DEN']))

	print(len(data[data.ORIGIN == 'DEN']))
	print(nx.info(gDEN))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gDEN, with_labels=True, **options)
	plt.show()




def jfk_function():
	print(gJFK.degree('JFK'))
	JFK_deg_cen = nx.degree_centrality(gJFK)
	print("The degree centrality of JFK:"+str(JFK_deg_cen['JFK']))
	JFK_clo_cen = nx.closeness_centrality(gJFK, distance='weight')
    
	print("The closeness centrality of JFK:"+str(JFK_clo_cen['JFK']))

	print(len(data[data.ORIGIN == 'JFK']))
	print(nx.info(gJFK))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gJFK, with_labels=True, **options)
	plt.show()




def las_function():
	print(gLAS.degree('LAS'))
	LAS_deg_cen = nx.degree_centrality(gLAS)
	print("The degree centrality of LAS:"+str(LAS_deg_cen['LAS']))
	LAS_clo_cen = nx.closeness_centrality(gLAS, distance='weight')
    
	print("The closeness centrality of LAS:"+str(LAS_clo_cen['LAS']))

	print(len(data[data.ORIGIN == 'LAS']))
	print(nx.info(gLAS))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gLAS, with_labels=True, **options)
	plt.show()




def sfo_function():
	print(gSFO.degree('SFO'))
	SFO_deg_cen = nx.degree_centrality(gSFO)
	print("The degree centrality of SFO:"+str(SFO_deg_cen['SFO']))
	SFO_clo_cen = nx.closeness_centrality(gSFO, distance='weight')
    
	print("The closeness centrality of SFO:"+str(SFO_clo_cen['SFO']))

	print(len(data[data.ORIGIN == 'SFO']))
	print(nx.info(gSFO))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gSFO, with_labels=True, **options)
	plt.show()




def sea_function():
	print(gSEA.degree('SEA'))
	SEA_deg_cen = nx.degree_centrality(gSEA)
	print("The degree centrality of SEA:"+str(SEA_deg_cen['SEA']))
	SEA_clo_cen = nx.closeness_centrality(gSEA, distance='weight')
    
	print("The closeness centrality of SEA:"+str(SEA_clo_cen['SEA']))

	print(len(data[data.ORIGIN == 'SEA']))
	print(nx.info(gSEA))
	options = {
        'node_size': 10,
        'width': 0.5,
    }
	nx.draw(gSEA, with_labels=True, **options)
	plt.show()


draw("whole")
# draw("LAX")
# draw("CLT")
# draw("ORD")
# draw("DAL")
# draw("DEN")
# draw("JFK")
# draw("LAS")
# draw("SFO")
# draw("SEA")