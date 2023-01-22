num1 = int(input())
num2 = int(input())
magic_num = int(input())

flag = False
magic_num_count = 0

for a in range(num1, num2 + 1):
    for b in range(num1, num2 + 1):
        magic_num_count += 1
        if a + b == magic_num:
            flag = True
            break
    if a + b == magic_num:
        break

if flag:
    print(f"Combination N:{magic_num_count} ({a} + {b} = {magic_num})")
else:
    print(f"{magic_num_count} combinations - neither equals {magic_num}")
