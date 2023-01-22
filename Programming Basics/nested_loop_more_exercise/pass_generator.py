n1 = int(input())
n2 = int(input())
ord_num = 97 + n2

for i in range(1, n1):
    for j in range(1, n1):
        for k in range(97, ord_num):
            for g in range(97, ord_num):
                for l in range(1, n1 + 1):
                    if (l > i) and (l > j):
                        print(f"{i}{j}{chr(k)}{chr(g)}{l}", end=" ")
