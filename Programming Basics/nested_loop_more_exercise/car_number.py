first_num = int(input())
last_num = int(input())

for i in range(first_num, last_num + 1):
    if i % 2 == 0:
        for k in range(first_num, last_num + 1):
            for l in range(first_num, last_num + 1):
                if (k + l) % 2 == 0:
                    for h in range(first_num, last_num + 1):
                        if h % 2 != 0 and h < i:
                            print(f"{i}{k}{l}{h}", end=" ")

    if i % 2 != 0:
        for k in range(first_num, last_num + 1):
            for l in range(first_num, last_num + 1):
                if (k + l) % 2 == 0:
                    for h in range(first_num, last_num + 1):
                        if h % 2 == 0 and h < i:
                            print(f"{i}{k}{l}{h}", end=" ")
