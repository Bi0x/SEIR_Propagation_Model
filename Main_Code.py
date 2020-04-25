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

infectionStart(safe, incubation, infected, recOrDead, mapData,
               iterTime=t, omega=Omega, beta=Beta, mu=Mu)


plt.show()
