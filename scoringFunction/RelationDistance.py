from dataLoader.IDataStructure import IRpaData
from scipy.spatial import distance


def getRelationDistance(canvasDataArray):
    attributeLocation = {}
    for document in canvasDataArray:
        for link in document.info.linkDisplacement:
            attributeLocation[link.attributeCode] = (link.coordinates["x"], link.coordinates["y"])
    # print(attributeLocation)

    for document in canvasDataArray:
        for link in document.linkInfo:
            a1 = link.startPoint
            a2 = link.destination
            p1 = attributeLocation[a1]
            p2 = attributeLocation[a2]
            d = distance.euclidean(p1, p2)
            # print(a1, a2, d)

    return 0

