from ERNetwork import *
from SEIRModel import *
import time

startTime = time.time()
# ER Network Create
pointSum = 1000
connectProbability = 0.006

# SEIR Model
Omega = 0.2
Beta = 0.5
Mu = 0.2
t = 100
loopTime = 100
firstLoop = 1

totalSafeCount = []
totalIncubationCount = []
totalInfectedCount = []
totalRecOrDeadCount = []

for i in range(loopTime):
    mapData = createERNetwork(pointSum, connectProbability)
    #createDegreeChart(mapData, pointSum)
    #drawERMap(mapData)

    safe = [x for x in range(1, pointSum + 1)]
    incubation = []
    infected = []
    recOrDead = []

    firstInfector = firstInfectorSelect(pointSum)
    safe.remove(firstInfector)
    infected.append(firstInfector)

    safeCount = [pointSum - 1]
    incubationCount = [0]
    infectedCount = [1]
    recOrDeadCount = [0]

    infectionStart(safe, incubation, infected, recOrDead, 
                safeCount, incubationCount, infectedCount, recOrDeadCount, 
                mapData, iterTime=t, omega=Omega, beta=Beta, mu=Mu)
    
    if firstLoop == 1:
        totalSafeCount = safeCount.copy()
        totalIncubationCount = incubationCount.copy()
        totalInfectedCount = infectedCount.copy()
        totalRecOrDeadCount = recOrDeadCount.copy()
        firstLoop = 0
    else:
        for j in range(t + 1):
            totalSafeCount[j] += safeCount[j]
            totalIncubationCount[j] += incubationCount[j]
            totalInfectedCount[j] += infectedCount[j]
            totalRecOrDeadCount[j] += recOrDeadCount[j]
    print("Now running case: " + str(i + 1))

for i in range(t + 1):
    totalSafeCount[i] /= loopTime
    totalIncubationCount[i] /= loopTime
    totalInfectedCount[i] /= loopTime
    totalRecOrDeadCount[i] /= loopTime

drawCurveChart(totalSafeCount, totalIncubationCount, totalInfectedCount, totalRecOrDeadCount, iterTime=t)

#print(time.time() - startTime)
plt.show()
