from dataLoader import constants


def getPartitionPercentage(canvasDataArray):
    percentage = {}
    categoryA = 0
    categoryB = 0
    categoryC = 0
    maxWidth = 0

    for document in canvasDataArray:
        category = document.info.category
        width = document.info.width
        if width > maxWidth:
            maxWidth = width
        if category == 'A':
            categoryA = categoryA + 1
        elif category == 'B':
            categoryB = categoryB + 1
        elif category == 'C':
            categoryC = categoryC + 1

    sum = categoryA + categoryB + categoryC

    pixelA = (categoryA / sum) * constants.screenWidth
    pixelB = (categoryB / sum) * constants.screenWidth
    pixelC = (categoryC / sum) * constants.screenWidth

    if maxWidth > pixelA:
        pixelA = maxWidth + 20
    if maxWidth > pixelB:
        pixelB = maxWidth + 20
    if maxWidth > pixelC:
        pixelC = maxWidth + 20

    percentage['A'] = pixelA
    percentage['B'] = pixelB
    percentage['C'] = pixelC

    return percentage
