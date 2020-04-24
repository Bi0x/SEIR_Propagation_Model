import networkx as nx
import matplotlib.pyplot as plt 
import random

def createERNetwork(pointSum = 10, connectProbability = 0.2):
    graphData = nx.Graph()
    for i in range(pointSum):
        for j in range(pointSum):
            if i == j:
                continue
            p = random.random()
            if p > connectProbability:
                continue
            graphData.add_edge(i, j)
    return graphData

def drawERMap(graphData):
    plt.figure()
    plt.title("ER Networks", fontsize = 15)
    pos = nx.spring_layout(graphData, iterations=200)
    nx.draw(graphData, pos, with_labels = True, node_size = 200, node_color = 'lightblue')

def createDegreeChart(graphData):
    return