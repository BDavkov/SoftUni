num1 = int(input())
num2 = int(input())
magic_number = int(input())
count = 0
flag = False
correct_num1 = 0
correct_num2 = 0

for i in range(num1, num2 + 1):
    if flag:
        break

    for k in range(num1, num2 + 1):
        count += 1
        if i + k == magic_number:
            flag = True
            correct_num1 = i
            correct_num2 = k
            break


if flag:
    print(f"Combination N:{count} ({correct_num1} + {correct_num2} = {magic_number})")
else:
    print(f"{count} combinations - neither equals {magic_number}")
