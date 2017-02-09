T  = int(input());

for i in range(1,T+1):
    (L,R) = map(int, input().split(" "));
    val = min(L,R);
    #print(val);
    if(val==0):
        print("Case #{}: 0".format(i));
    else:
        calc = (val*(val+1))/2;
        val2 = str(int(calc));
        print("Case #{}: {}".format(i, val2));
