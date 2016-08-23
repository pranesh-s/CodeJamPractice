#Using numpy for easy array management
import numpy as np;

t = int(input());

for i in range(1, t+1):
    criteria = input().split(" ");

    # Load input into array
    manipArr = np.zeros((int(criteria[0]), int(criteria[0])), dtype=np.str);
    for x in range(0, int(criteria[0])):
        temp = input();
        for y in range(0, int(criteria[0])):
            manipArr[x][y] = temp[y];

    # Apply "rotation"
    for x in range(0, int(criteria[0])):
        for y in range(int(criteria[0])-1, -1, -1):
            if manipArr[x][y] == '.':
                currY = y;
                while (manipArr[x][currY]!='R' and manipArr[x][currY]!='B' and currY>0):
                    currY-=1;

                manipArr[x][y] = manipArr[x][currY];
                manipArr[x][currY] = '.';

    # Boolean flags
    redWin = False;
    blueWin = False;

    # Integer storing win length
    inarow = int(criteria[1]);

    # Win checker
    for x in range(0, int(criteria[0])):
        for y in range(0, int(criteria[0])):
            if manipArr[x][y]!='.' and (not redWin or not blueWin):
                if x-inarow >= -1:
                    countTokens = 0;
                    for a in range(x, (x-inarow+1), -1):
                        if manipArr[a][y] == manipArr[a-1][y]:
                            countTokens+=1;
                        else:
                            break;
                    if countTokens == (inarow-1):
                        if manipArr[x][y] == 'R':
                            redWin = True;
                        else:
                            blueWin = True;
                if y-inarow >= -1:
                    countTokens = 0;
                    for a in range(y, (y-inarow+1), -1):
                        if manipArr[x][a] == manipArr[x][a-1]:
                            countTokens+=1;
                        else:
                            break;
                    if countTokens == (inarow-1):
                        if manipArr[x][y] == 'R':
                            redWin = True;
                        else:
                            blueWin = True;
                if y-inarow >= -1 and x-inarow >=-1:
                    countTokens = 0;
                    for a,b in zip(range(x, (x-inarow+1), -1), (range(y, (y-inarow+1), -1))):
                        if manipArr[a][b] == manipArr[a-1][b-1]:
                            countTokens+=1;
                        else:
                            break;
                        if countTokens == (inarow-1):
                            if manipArr[x][y] == 'R':
                                redWin = True;
                            else:
                                blueWin = True;
                if y-inarow>= -1 and x+inarow <= int(criteria[0]):
                    countTokens = 0;
                    for a,b in zip(range(x, (x+inarow+1)), (range(y, (y-inarow+1), -1))):
                        if manipArr[a][b] == manipArr[a+1][b-1]:
                            countTokens+=1;
                        else:
                            break;
                        if countTokens == (inarow-1):
                            if manipArr[x][y] == 'R':
                                redWin = True;
                            else:
                                blueWin = True;

    if(blueWin and redWin):
        print("Case #{}: Both".format(i));
    elif (blueWin):
        print("Case #{}: Blue".format(i));
    elif (redWin):
        print("Case #{}: Red".format(i));
    else:
        print("Case #{}: Neither".format(i));
