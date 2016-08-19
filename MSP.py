import numpy as np

t = int(input());

for i in range (1, t+1):
    vecNumber = int(input());
    firstList = [int(s) for s in input().split(" ")];
    secondList = [int (u) for u in input().split(" ")];
    firstList.sort();
    secondList.sort(reverse=True);
    output = np.dot(firstList, secondList);
    print("Case #{}: {}".format(i, output));
