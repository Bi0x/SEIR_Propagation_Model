import random


def firstInfectorSelect(pointSum):
    return random.randint(1, pointSum)


def infectionStart(safe, incubation, infected, recOrDead, graphData, iterTime=100, omega=0.2, beta=0.5, mu=0.2):
    for ti in range(iterTime):
        newInfect = []
        newIncubation = []
        newRecOrDead = []
        # Infect Neighbors
        for infector in infected:
            neighbors = graphData.neighbors(infector)
            for nei in neighbors:
                if random.random() > omega:
                    continue
                if nei in safe:
                    newIncubation.append(nei)
        # Incubation recovery or dead
        for incu in incubation:
            if random.random() > mu:
                if random.random() > beta:
                    continue
                newInfect.append(incu)
            else:    
                newRecOrDead.append(incu)
        
