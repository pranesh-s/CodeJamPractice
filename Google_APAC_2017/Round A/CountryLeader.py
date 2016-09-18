t = int(input());

for i in range(1, t+1):
    N = int(input());
    maxArr = [0, 0];
    output = "";
    for j in range(0, N):
        nameInit = input();
        name = nameInit.replace(' ', '');

        if len(name)< maxArr[1]:
            continue;

        newName = "".join(set(name));

        if len(newName) > maxArr[0]:
            maxArr[0] = len(newName);
            output = nameInit;
        elif len(newName)==maxArr[0]:
            for x in range(0, len(nameInit)):
                charValLocal = ord(nameInit[x])-64;
                if x>=len(output):
                    break;
                charValOld = ord(output[x]) - 64;
                if charValLocal<charValOld:
                    output = nameInit;
                    break;
                elif charValLocal>charValOld:
                    break;
                if x == len(nameInit) - 1 and len(output)>len(nameInit):
                    output = nameInit;
                    break;
    print("Case #{}: {}".format(i, output));
