import requests
from dataLoader.IDataStructure import IRpaData


def getData():

    response = requests.post("http://localhost:8000/space-mongo-server/logData",
                             {
                                 "collectionName": "rpaData",
                                 "msId": "9EfnEpevW2KN9uuH5Cj5"
                             })

    responseJSON = response.json()
    payload = responseJSON["payload"]

    canvasDataArray = []

    for document in payload:
        dataObject = IRpaData(
            document["entityCode"],
            document["info"],
            document["linkInfo"]
        )
        canvasDataArray.append(dataObject)

    # for i in canvasDataArray:
    #     print(i.info.category)

    return canvasDataArray
    # for i in a:
    #     for j in i.info.linkDisplacement:
    #         print(j.attributeCode, j.coordinates["x"])


