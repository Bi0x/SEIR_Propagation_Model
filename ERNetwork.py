import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


def createERNetwork(pointSum=10, connectProbability=0.2):
    graphData = nx.Graph()
    for i in range(pointSum):
        for j in range(i + 1, pointSum):
            if i == j:
                continue
            p = random.random()
            if p > connectProbability:
                continue
            graphData.add_edge(i, j)
    return graphData


def drawERMap(graphData):
    plt.figure()
    plt.title("ER Networks", fontsize=15)
    pos = nx.spring_layout(graphData, iterations=200)
    nx.draw(graphData, pos, with_labels=True,
            node_size=200, node_color='lightblue')


def createDegreeChart(graphData, pointSum):
    maxDegree = 0
    for i in range(pointSum):
        try:
            maxDegree = max(maxDegree, graphData.degree(i))
        except nx.exception.NetworkXError:
            pass
    #print(maxDegree)
    plt.figure()
    plt.title("Degree Distribution Chart", fontsize=15)
    degreeData = [0] * (maxDegree + 1)
    for i in range(pointSum):
        try:
            degreeData[graphData.degree(i)] += 1
        except nx.exception.NetworkXError:
            degreeData[0] += 1
    for i in range(len(degreeData)):
        degreeData[i] = degreeData[i] * 1.0 / pointSum
    xLine = [x for x in range(maxDegree + 1)]
    yLine = degreeData
    plt.plot(xLine, yLine, marker='o')