

from dataLoader.load import *
from dataLoader.CalculatePartition import *
from scoringFunction.ScoringFunction import *

canvasDataArray = getData()
partitionPixels = getPartitionPercentage(canvasDataArray)

# print(partitionPixels)

for i in canvasDataArray:
    for j in i.linkInfo:
        print(j.destination)

score = getScore()
print(score)

