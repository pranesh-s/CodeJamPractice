import numpy as np;
import math

#np.set_printoptions(threshold=np.inf);

t = int(input());

def dfs(inputGraph, v, labelArr, visited):
    i = v[0];
    j = v[1];
    I = np.shape(inputGraph)[0];
    J = np.shape(inputGraph)[1];
    retArr = [1, 1, 1, 1];
    curr = inputGraph[i][j];

    comparator = math.inf;
    minSeen = [];
    visited.append(v);

    if (i <= 0 or j <= 0 or i>=(I-1) or j>=(J-1)):
        return 0, [-1], visited;
    if (inputGraph[i-1][j]<curr or inputGraph[i+1][j]<curr or inputGraph[i][j-1]<curr or inputGraph[i][j+1]<curr):
        return 0, [-1], visited;

    labelArr[i][j] = 1;

    if (labelArr[i-1][j] == 0 and inputGraph[i-1][j] == curr):
        out1 = dfs(inputGraph, (i-1, j), labelArr, visited);
        retArr[0] = out1[0];
        minSeen.append(min(out1[1]));
    elif (labelArr[i-1][j] == 0):
        minSeen.append(inputGraph[i-1][j]);
    if (labelArr[i+1][j] == 0 and inputGraph[i+1][j] == curr):
        out2 = dfs(inputGraph, (i+1, j), labelArr, visited);
        retArr[1] = out2[0];
        minSeen.append(min(out2[1]));
    elif labelArr[i+1][j] == 0:
        minSeen.append(inputGraph[i+1][j]);
    if (labelArr[i][j-1] == 0 and inputGraph[i][j-1] == curr):
        out3 = dfs(inputGraph, (i, j-1), labelArr, visited);
        retArr[2] = out3[0];
        minSeen.append(min(out3[1]));
    elif labelArr[i][j-1]==0:
        minSeen.append(inputGraph[i][j-1]);
    if (labelArr[i][j+1] == 0 and inputGraph[i][j+1] == curr):
        out4 = dfs(inputGraph, (i, j+1), labelArr, visited);
        retArr[3] = out4[0];
        minSeen.append(min(out4[1]));
    elif labelArr[i][j+1]==0:
        minSeen.append(inputGraph[i][j+1]);

    if not minSeen:
        minReturn = comparator;
    else:
        minReturn = min(minSeen);
    return (1 * (retArr[0] * retArr[1] * retArr[2] * retArr[3])), [minReturn], visited;
for i in range(1, t+1):
    I,J = map(int, input().split(" "));

    island = np.empty((I, J), dtype=np.int);
    for x in range(0, I):
        l = [int(s) for s in input().split(" ")];
        for y in range(0, J):
            island[x][y] = l[y];

    totalSum = 0;
    for g in range(0, 1000):
        for a in range(0, I):
            for b in range(0, J):
                if(island[a][b] == g):
                    labelArr = np.zeros(np.shape(island), dtype = np.int);
                    visited = [];
                    returnedV = dfs(island, (a,b), labelArr, visited);
                    if(returnedV[0]>0):
                        for coord in returnedV[2]:
                            adding = (returnedV[1][0] - island[coord[0]][coord[1]]);
                            ## DEBUG ##
                            if adding<=0:
                                print("WARNING ADDING By <=0: ", adding);
                            ## DEBUG ##
                            totalSum+=adding;
                            island[coord[0]][coord[1]] = returnedV[1][0];
    print("Case #{}: {}".format(i, totalSum));
