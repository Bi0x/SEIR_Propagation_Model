from ERNetwork import *
from SEIRModel import *

# ER Network Create
pointSum = 10
connectProbability = 0.2

mapData = createERNetwork(pointSum, connectProbability)
drawERMap(mapData)
createDegreeChart(mapData, pointSum)


# SEIR Model
Omega = 0.2
Beta = 0.5
Mu = 0.2
t = 100

safe = [x for x in range(1, pointSum + 1)]
incubation = []
infected = []
recOrDead = []

firstInfector = firstInfectorSelect(pointSum)
safe.remove(firstInfector)
infected.append(firstInfector)

safeCount = pointSum - 1
incubationCount = 0
infectedCount = 1
recOrDeadCount = 0

infectionStart(safe, incubation, infected, recOrDead, 
               safeCount, incubationCount, infectedCount, recOrDeadCount, 
               mapData, iterTime=t, omega=Omega, beta=Beta, mu=Mu)


plt.show()
