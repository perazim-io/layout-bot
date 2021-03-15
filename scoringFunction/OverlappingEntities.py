from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def getOverlappingEntities(canvasDataArray):
    overlapCount = 0
    for document in canvasDataArray:
        loc = getCoordinates(document)
        for newDocument in canvasDataArray:
            newLoc = getCoordinates(newDocument)
            if loc == newLoc:
                continue
            else:
                polygon = Polygon(loc)
                for i in newLoc:
                    point = Point(i)
                    if polygon.contains(point):
                        overlapCount = overlapCount + 1
                        break

    # print(overlapCount/2)
    # print(newLoc)
    # print(newLoc[0][0])
    return overlapCount


def getCoordinates(document):
    location = document.info.location
    loc = (location.split())
    newLoc = []
    x = float(loc[0])
    y = float(loc[1])
    newLocList = (x, y)
    newLoc.append(newLocList)
    height = document.info.height
    width = document.info.width
    newLoc.append((x+width, y))
    newLoc.append((x+width, y+height))
    newLoc.append((x, y+height))
    return newLoc
