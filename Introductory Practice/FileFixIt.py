t = int(input());

for i in range(1, t+1):
    directoryList = [];
    mkdirCount = 0;
    crit = input().split(" ");
    for x in range (0, int(crit[0])):
        obsStr = [("/" + s) for s in filter(bool, input().split("/"))];
        addToList = "";
        for y in range(0, len(obsStr)):
            addToList = addToList + obsStr[y];
            directoryList.append(addToList);
    for z in range(0, int(crit[1])):
        temp = [("/" + s) for s in filter(bool, input().split("/"))];
        dirListObs = [];
        if temp not in directoryList:
            checkVal = "";
            for y in range(0, len(temp)):
                checkVal = checkVal + temp[y];
                if checkVal not in directoryList:
                    mkdirCount+=1;
                    directoryList.append(checkVal);
    print("Case #{}: {}".format(i, mkdirCount));
