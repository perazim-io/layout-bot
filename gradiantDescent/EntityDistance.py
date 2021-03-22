from scipy.spatial import distance


def getRelationDistance(entityData, x=650, y=740):
    location = entityData.info.location
    loc = location.split()
    x1 = float(loc[0])
    y1 = float(loc[1])
    p = (x1, y1)
    xFixed = getDistanceDictionaryX(p[0], x, y)
    yFixed = getDistanceDictionaryY(p[1], x, y)
    print(xFixed)
    return 0


def getDistanceDictionaryX(coord, x, y):
    point1 = (x, y)
    xFixed = {point1: []}
    for i in range(1079):
        point2 = (coord, i)
        d = distance.euclidean(point1, point2)
        xFixed[point1].append([point2, d])
    return xFixed


def getDistanceDictionaryY(coord, x, y):
    point1 = (x, y)
    yFixed = {point1: []}
    for i in range(1079):
        point2 = (i, coord)
        d = distance.euclidean(point1, point2)
        yFixed[point1].append([point2, d])
    return yFixed
