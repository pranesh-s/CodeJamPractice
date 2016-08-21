import numpy as np;

t = int(input());

for i in range(1, t+1):
    criteria = input().split(" ");

    manipArr = np.zeros((int(criteria[0]), int(criteria[0])), dtype=np.int);
    for x in range(0, int(criteria[0])):
        temp = input();
        for y in range(0, int(criteria[0])):
            if temp[y] is '.':
                manipArr[x][y] = 0;
            elif temp[y] is 'R':
                manipArr[x][y] = 1;
            elif temp[y] is 'B':
                manipArr[x][y] = 2;

    for x in range(0, int(criteria[0])):
        for y in range(int(criteria[0])-1, -1, -1):
            if manipArr[x][y] == 0:
                currY = y;
                while (manipArr[x][currY]!=1 and manipArr[x][currY]!=2 and currY>0):
                    currY-=1;

                manipArr[x][y] = manipArr[x][currY];
                manipArr[x][currY] = 0;
    redWin = False;
    blackWin = False;
    inarow = int(criteria[1]);
    for x in range(0, int(criteria[0])):
        for y in range(0, int(criteria[0])):
            if manipArr[x][y]!=0:
                if x-inarow >= -1:
                    countR = 0;
                    countB = 0;
                    for a in range(x, (x-inarow+1), -1):
                        if manipArr[a][y] == 1 and manipArr[a-1][y] == 1:
                            countR+=1;
                        elif manipArr[a][y] == 2 and manipArr[a-1][y] == 2:
                            countB+=1;
                        else:
                            break;
                    if countR == (inarow-1):
                        redWin = True;
                    if countB == (inarow-1):
                        blackWin = True;
                if y-inarow >= -1:
                    countR = 0;
                    countB = 0;
                    for a in range(y, (y-inarow+1), -1):
                        if manipArr[x][a] == 1 and manipArr[x][a-1] == 1:
                            countR+=1;
                        elif manipArr[x][a] == 2 and manipArr[x][a-1] == 2:
                            countB+=1;
                        else:
                            break;
                    if countR == (inarow-1):
                        redWin = True;
                    if countB == (inarow-1):
                        blackWin = True;
                if y-inarow >= -1 and x-inarow >=-1:
                    countR = 0;
                    countB = 0;
                    for a,b in zip(range(x, (x-inarow+1), -1), (range(y, (y-inarow+1), -1))):
                        if manipArr[a][b] == 1 and manipArr[a-1][b-1] == 1:
                            countR+=1;
                        elif manipArr[a][b] == 2 and manipArr[a-1][b-1] == 2:
                            countB+=1;
                        else:
                            break;
                        if countR == (inarow-1):
                            redWin = True;
                        if countB == (inarow-1):
                            blackWin = True;
                if y-inarow>= -1 and x+inarow <= int(criteria[0]):
                    countR = 0;
                    countB = 0;
                    for a,b in zip(range(x, (x+inarow+1)), (range(y, (y-inarow+1), -1))):
                        if manipArr[a][b] == 1 and manipArr[a+1][b-1] == 1:
                            countR+=1;
                        elif manipArr[a][b] == 2 and manipArr[a+1][b-1] == 2:
                            countB+=1;
                        else:
                            break;
                        if countR == (inarow-1):
                            redWin = True;
                        if countB == (inarow-1):
                            blackWin = True;

    if(blackWin and redWin):
        print("Case #{}: Both".format(i));
    elif (blackWin):
        print("Case #{}: Blue".format(i));
    elif (redWin):
        print("Case #{}: Red".format(i));
    else:
        print("Case #{}: Neither".format(i));
