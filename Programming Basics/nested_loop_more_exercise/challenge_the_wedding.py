men = int(input())
women = int(input())
tables = int(input())
count = 0

for i in range(1, men + 1):
    for k in range(1, women + 1):
        if men <= 0 or women <= 0:
            break
        count += 1
        print(f"({i} <-> {k})", end=" ")
        if count == tables:
            break
    if count == tables:
        break
