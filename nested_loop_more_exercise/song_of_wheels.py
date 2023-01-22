num = int(input())
count = 0
flag = False
password = ""

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if ((i * j + k * l) == num) and (i < j) and (k > l):
                    print(f"{i}{j}{k}{l}", end=" ")
                    count += 1
                    if count == 4:
                        flag = True
                        password = str(i) + str(j) + str(k) + str(l)

if flag:
    print(f"\nPassword: {password}")
else:
    print(f"\nNo!")
