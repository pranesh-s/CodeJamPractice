t = int(input());

for i in range(1, t+1):
    z = input();
    z = z[0] + z + z[len(z)-1];
    count = 1;
    for j in range(1, len(z)-1):
        innerCount = len(set(z[j-1:j+2]));
        count*=innerCount;
        count%=1000000007;
    print("Case #{}: {}".format(i, count));
