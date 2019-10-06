def listexpander(biglist):

    newBigList = []

    for list in biglist:

        num = list[0]

        newlist0 = [num + 4]
        newlist1 = [num - 4]
        newlist2 = [num * 4]
        newlist3 = [num // 4]
        newBigListItem = [newlist0, newlist1, newlist2, newlist3]

        if len(list) > 1:
            i = 1
            while i < len(list):
                for smlist in newBigListItem:
                    smlist.append(list[i])
                i = i + 1

        newlist0.append("+")
        newlist1.append("-")
        newlist2.append("*")
        newlist3.append("/")

        for item in newBigListItem:
            newBigList.append(item)

    return newBigList


testlist = [[4]]
biggerList = listexpander(testlist)
evenBiggerList = listexpander(biggerList[0:])
biggestList = listexpander(evenBiggerList[0:])
print(biggestList)

fullInput = input().split()
numOf = int(fullInput[0])
importantInput = fullInput[1:numOf + 1]
for input in importantInput:
    nosolution = True
    input = int(input)
    for list in biggestList:
        if input == list[0]:
            nosolution = False
            print("4 " + list[1] + " 4 " + list[2] + " 4 " \
                + list[3] + " 4 = " + str(input))
            break
    if nosolution:
        print("no solution")
