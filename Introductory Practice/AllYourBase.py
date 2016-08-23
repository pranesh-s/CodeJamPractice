import numpy as np;

t = int(input());

for i in range(1, t+1):
    alienIn = input();
    alienOut = 0;
    debugOut = 0;
    # Generates alien dictionary
    alienDictionary = {alienIn[0]:1};
    for s in alienIn:
        if s not in alienDictionary:
            index = len(alienDictionary);
            if index == 1:
                alienDictionary[s] = 0;
            else:
                alienDictionary[s] = index;
    base = max(len(alienDictionary), 2);
    for x in range(0, len(alienIn)):
        alienOut = alienOut + (pow(base, len(alienIn)-x-1) * alienDictionary[alienIn[x]]);
    print("Case #{}: {}".format(i, alienOut));
