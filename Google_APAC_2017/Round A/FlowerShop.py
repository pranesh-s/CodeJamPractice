t = int(input());

# Used to calculate new range within which correct value of r is located
def calcNewRToCheck(start, end, calcVal):
    halfLength = (end-start)/2;
    if calcVal>0:
        newStart = start+halfLength;
        newEnd = end;
    elif calcVal < 0:
        newStart = start;
        newEnd = end-halfLength;
    newR = newStart+((newEnd-newStart)/2);
    return newStart, newEnd, newR;

# Used to calculate output of r
def calculateValue (r, readVals, timePeriod):
    rChanged = r+1;
    calc = 0;
    calc = -(readVals[0]) * pow((rChanged), timePeriod);
    for j in range(0, timePeriod):
        calc+= (readVals[j+1] * pow((rChanged), timePeriod-j-1));
    return calc;


for i in range(1, t+1):
    timePeriod = int(input());
    readVals = [int(s) for s in input().split(" ")];
    boundStart = -1;
    boundEnd = 1;
    correctAnswer = False;

    r = 0;
    while not correctAnswer:
        calc = calculateValue(r, readVals, timePeriod);
        if (calc==0):
            break;
        tempC = calcNewRToCheck(boundStart, boundEnd, calc);
        boundStart = (tempC[0]);
        boundEnd = (tempC[1]);
        rOld = r;
        r = tempC[2];
        if(abs(rOld-r) < pow(10, -9)):
            correctAnswer = True;

    print("Case #{}: {}".format(i, r));
