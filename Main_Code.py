from ERNetwork import *
from SEIRModel import *

# ER Network Create
pointSum = 20
connectProbability = 0.4
'''
mapData = createERNetwork(pointSum, connectProbability)
drawERMap(mapData)
createDegreeChart(mapData, pointSum)
'''

# SEIR Model
omega = 0.2
beta = 0.5
mu = 0.2
t = 100

safe = [x for x in range(1, pointSum + 1)]
incubation = []
infected = []
recordead = []

firstInfector = firstInfectorSelect(pointSum)
safe.remove(firstInfector)
infected.append(firstInfector)


# plt.show()
