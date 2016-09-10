t = int(input());


for i in  range(1, t+1):
    criteria = input().split(" ");
    list1 = input().split(" ");
    list2 = input().split(" ");
    list3 = input().split(" ");
    list4 = input().split(" ");

    N = int(criteria[0]);
    K = int(criteria[1]);

    answer = 0;
    dict_map = {};

    for j in range(0, N):
        for k in range(0, N):
            val_calculated = int(list1[j]) ^ int(list2[k]);
            if not val_calculated in dict_map:
                dict_map[val_calculated] = 1;
            else:
                dict_map[val_calculated] +=1;
    for j in range(0, N):
        for k in range(0, N):
            val_needed = (K^int(list3[j])^int(list4[k]));
            answer+= dict_map.get(val_needed, 0);
    print("Case #{}: {}".format(i, answer));
