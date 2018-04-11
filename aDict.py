def uniqueValues(aDict):
    dictValues = list(aDict.values())
    dictKeys = list(aDict.keys())
    dictValuesSorted = []
    mNumbers = []


    for value in dictValues:
        if dictValues.count(value) > 1:
            if(value not in mNumbers):
                mNumbers.append(value)

    for key in dictKeys:
        if(aDict[key] in mNumbers):
            del aDict[key]

    dictValuesSorted = list(aDict.keys())
    dictValuesSorted.sort()

    return list(dictValuesSorted)






dic = {3: 1, 1: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print(uniqueValues(dic))