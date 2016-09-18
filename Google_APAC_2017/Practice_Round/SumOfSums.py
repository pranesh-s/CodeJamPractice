t = int(input());

for i in range(1, t+1):
    N,Q = map(int, input().split(" "));

    initArray = [int(s) for s in input().split(" ")];

    modList = [];
    count = 0;
    outDebugBills = 0;
    for x in range(0, N):
        for y in range(0, N):
            if (y+x <= N):
                toAppend = sum(initArray[(y): (y+x)])
                modList.append(toAppend);
        print("we are looking at position: ", x);
    modList = sorted(modList);
    print("InitArray length is: ", len(initArray));
    print("ModList length is: ", len(modList));
    print("Length should be: ", ((N*(N+1)/2)));
    print("Case #{}:".format(i));
    for x in range(0, Q):
        L,R = map(int, input().split(" "));
        output = sum(modList[L-1:R]);
        print(output);
