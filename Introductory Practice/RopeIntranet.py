t = int(input());

for i in range(1, t+1):
    s = int(input());
    ropeList = [];
    intersectionCount = 0;
    for u in range(0, s):
        ropeList.append(input());
    for x in range(0, s):
        for y in range(x+1, s):
            ropeOne = [int(v) for v in ropeList[x].split(" ")];
            ropeTwo = [int(v) for v in ropeList[y].split(" ")];
            if ((ropeOne[0] -ropeTwo[0] )* (ropeOne[1]-ropeTwo[1]) < 0):
                intersectionCount+=1;
    print("Case #{}: {}".format(i, intersectionCount));
