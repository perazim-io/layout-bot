
class linkDisplacementData:

    def __init__(self, attributeCode, coordinates):
        self.attributeCode = attributeCode
        self.coordinates = coordinates


class RpaEntityData(linkDisplacementData):

    def __init__(self, info):
        self.height = info["height"]
        self.location = info["location"]
        if hasattr(info, 'newLocation'):
            self.newLocation = info["newLocation"]
        self.width = info["width"]
        self.outLinksCnt = info["outLinksCnt"]
        self.inLinksCnt = info["inLinksCnt"]
        self.outPortsCnt = info["outPortsCnt"]
        self.inPortsCnt = info["inPortsCnt"]
        self.linkDisplacement = []
        for i in info["linkDisplacement"]:
            self.linkDisplacement.append(linkDisplacementData(i["attributeCode"], i["coordinates"]))



class IRpaData(RpaEntityData):

    def __init__(self, entityCode, info):
        self.entityCode = entityCode
        self.info = RpaEntityData(info)