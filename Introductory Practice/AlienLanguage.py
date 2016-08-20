import numpy as np;

def checkStringBitmap(bitMap, string):
    count = 0;
    for char in string:
        charVal = abs(97-ord(char));
        if(bitMap[charVal][count] == 1):
            count+=1;
        else:
            return False;
    return True;

criteria = [int(s) for s in (input().split(" "))];
alphabetList= [];

caseStart = 1+criteria[1];
caseEnd = caseStart+criteria[2];

for x in range(0, criteria[1]):
    alphabetList.append(input());

for c in range(caseStart, caseEnd):
    bitMap = np.zeros((26, criteria[0]), dtype=np.int);
    count = 0;
    bracketFlag = 0;
    currentReference = input();
    for char in (currentReference):
        charVal = abs(97-ord(char));
        if ord(char) == 40:
            bracketFlag = 1;
        elif ord(char) == 41:
            bracketFlag = 0;
            count+=1;
        elif bracketFlag == 1:
            bitMap[charVal][count] = 1;
        else:
            bitMap[charVal][count] = 1;
            count+=1;
    outputCount = 0;
    caseNumber = abs(caseStart-c)+1;
    for alpha in alphabetList:
        if (checkStringBitmap(bitMap, alpha)):
            outputCount+=1;
    print("Case #{}: {}".format(caseNumber, outputCount));
