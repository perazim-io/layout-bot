

from dataLoader.load import *
from dataLoader.CalculatePartition import *

canvasDataArray = getData()
partitionPercentage = getPartitionPercentage(canvasDataArray)

print(partitionPercentage)