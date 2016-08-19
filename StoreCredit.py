t = int(input())

for i in range(1, t + 1):
  c = [int(input())]
  items = [int(input())]
  l = [int(s) for s in input().split(" ")]

  for x in range(0, items[0]):
      for y in range(x+1, items[0]):
          if(l[x]+l[y] == c[0]):
              if(x<y):
                  print("Case #{}: {} {}".format(i, x+1, y+1))

              else:
                  print("Case #{}: {} {}".format(i, y+1, x+1))
                  raise
