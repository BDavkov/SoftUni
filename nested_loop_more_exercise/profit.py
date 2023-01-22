lev1 = int(input())
lev2 = int(input())
lev5 = int(input())
change = int(input())

for i in range(lev1 + 1):
    for k in range(lev2 + 1):
        for j in range(lev5 + 1):
            current1 = i
            current2 = k * 2
            current5 = j * 5
            if current1 + current2 + current5 == change:
                print(f"{i} * 1 lv. + {k} * 2 lv. + {j} * 5 lv. = {change} lv.")