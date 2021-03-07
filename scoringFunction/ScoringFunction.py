from dataLoader.load import *
from scoringFunction.OverlappingEntities import *
from scoringFunction.RelationDistance import *


def getScore():
    score = 0
    canvasDataArray = getData()
    score = score + getOverlappingEntities(canvasDataArray) + getRelationDistance(canvasDataArray)
    return score



