t = int(input());

for i in range(1, t+1):
    sentence = input().split(" ");
    print("Case #{}: ".format(i), end='');
    for x in range(len(sentence)-1, -1, -1):
        print(sentence[x], end=' ');
    print("\n");
