

def getPartitionPercentage(canvasDataArray):

    percentage = {}
    categoryA = 0
    categoryB = 0
    categoryC = 0
    for document in canvasDataArray:
        category = document.info.category
        if category == 'A':
            categoryA = categoryA+1
        elif category == 'B':
            categoryB = categoryB+1
        elif category == 'C':
            categoryC = categoryC+1

    sum= categoryA + categoryB + categoryC

    percentageA = (categoryA/sum) * 100
    percentageB = (categoryB/sum) * 100
    percentageC = (categoryC/sum) * 100

    percentage['A'] = percentageA
    percentage['B'] = percentageB
    percentage['C'] = percentageC

    return percentage