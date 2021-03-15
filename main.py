

from dataLoader.load import *
from dataLoader.CalculatePartition import *
from scoringFunction.ScoringFunction import *
from gradiantDescent.EntityDistance import *

canvasDataArray = getData()
partitionPixels = getPartitionPercentage(canvasDataArray)

# print(partitionPixels)
#
# for i in canvasDataArray:
#     for j in i.linkInfo:
#         print(j.destination)

print(getRelationDistance(canvasDataArray[0]));
# score = getDistance(canvasDataArray[0]);

