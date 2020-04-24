from ERNetwork import *

pointSum = 10
connectProbability = 0.1
mapData = createERNetwork(pointSum, connectProbability)
drawERMap(mapData)
createDegreeChart(mapData, pointSum)

plt.show()
