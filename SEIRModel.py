import matplotlib.pyplot as plt
import random


def firstInfectorSelect(pointSum):
    return random.randint(1, pointSum)


def infectionStart(safe, incubation, infected, recOrDead,
                   safeCount, incubationCount, infectedCount, recOrDeadCount,
                   graphData, iterTime=100, omega=0.2, beta=0.5, mu=0.2):
    for ti in range(iterTime):
        newIncubation = []
        newInfected = []
        newRecOrDeadFromIncu = []
        newRecOrDeadFromInfec = []

        # Infecting neighbors
        for sa in safe:
            try:
                neighbors = graphData.neighbors(sa)
                infectedNeighbors = 0
                for nei in neighbors:
                    if nei in infected:
                        infectedNeighbors += 1
                if random.random() > (1 - (1 - omega) ** infectedNeighbors):
                    continue
                newIncubation.append(sa)
            except:
                pass

        # Incubation recovery or dead
        for incu in incubation:
            if random.random() > mu:
                if random.random() > beta:
                    continue
                newInfected.append(incu)
            else:
                newRecOrDeadFromIncu.append(incu)

        # Infected recovery or dead
        for infec in infected:
            if random.random() > mu:
                continue
            newRecOrDeadFromInfec.append(infec)

        # Round Summary
        newSafeCount = safeCount[-1]
        newIncubationCount = incubationCount[-1]
        newInfectedCount = infectedCount[-1]
        newRecOrDeadCount = recOrDeadCount[-1]
        for newIncu in newIncubation:
            safe.remove(newIncu)
            incubation.append(newIncu)
            newSafeCount -= 1
            newIncubationCount += 1
        for newInfec in newInfected:
            incubation.remove(newInfec)
            infected.append(newInfec)
            newIncubationCount -= 1
            newInfectedCount += 1
        for newROD in newRecOrDeadFromIncu:
            incubation.remove(newROD)
            recOrDead.append(newROD)
            newIncubationCount -= 1
            newRecOrDeadCount += 1
        for newROD in newRecOrDeadFromInfec:
            infected.remove(newROD)
            recOrDead.append(newROD)
            newInfectedCount -= 1
            newRecOrDeadCount += 1
        safeCount.append(newSafeCount)
        incubationCount.append(newIncubationCount)
        infectedCount.append(newInfectedCount)
        recOrDeadCount.append(newRecOrDeadCount)


def drawCurveChart(safeCount, incubationCount, infectedCount, recOrDeadCount, iterTime=100):
    plt.figure()
    plt.title('SEIR Model Results', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('N(t)', fontsize=12)
    xLine = [x for x in range(iterTime + 1)]
    plt.plot(xLine, safeCount, color='green', label='S', marker='o')
    plt.plot(xLine, incubationCount, color='red', label='E', marker='s')
    plt.plot(xLine, infectedCount, color='blue', label='I', marker='^')
    plt.plot(xLine, recOrDeadCount, color='orange', label='R', marker='v')
    plt.legend()
