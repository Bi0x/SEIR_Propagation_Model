from ERNetwork import *

pointSum = 20
connectProbability = 0.4
mapData = createERNetwork(pointSum, connectProbability)
drawERMap(mapData)
createDegreeChart(mapData, pointSum)

plt.show()
