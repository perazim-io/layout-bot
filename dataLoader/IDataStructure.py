class linkDisplacementData:
    def __init__(self, attributeCode, coordinates):
        self.attributeCode = attributeCode
        self.coordinates = coordinates


class linkData:
    def __init__(self, startPoint, destination):
        self.startPoint = startPoint
        self.destination = destination


class RpaEntityData(linkDisplacementData):
    def __init__(self, info):
        self.height = info["height"]
        self.location = info["location"]
        if hasattr(info, 'newLocation'):
            self.newLocation = info["newLocation"]
        self.category = info["category"]
        self.width = info["width"]
        self.outLinksCnt = info["outLinksCnt"]
        self.inLinksCnt = info["inLinksCnt"]
        self.outPortsCnt = info["outPortsCnt"]
        self.inPortsCnt = info["inPortsCnt"]
        self.linkDisplacement = []
        for i in info["linkDisplacement"]:
            self.linkDisplacement.append(linkDisplacementData(i["attributeCode"], i["coordinates"]))


class IRpaData(RpaEntityData, linkData):
    def __init__(self, entityCode, info, linkInfo):
        self.entityCode = entityCode
        self.info = RpaEntityData(info)
        self.linkInfo = []
        for i in linkInfo:
            self.linkInfo.append(linkData(i["from"], i["to"]))
