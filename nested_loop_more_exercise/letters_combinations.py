first_letter = input()
last_letter = input()
miss_letter = input()
count = 0

ord_first_letter = ord(first_letter)
ord_last_letter = ord(last_letter)
ord_miss_letter = ord(miss_letter)

for i in range(ord_first_letter, ord_last_letter + 1):
    if i == ord_miss_letter:
        continue
    for k in range(ord_first_letter, ord_last_letter + 1):
        if k == ord_miss_letter:
            continue
        for j in range(ord_first_letter, ord_last_letter + 1):
            if j == ord_miss_letter:
                continue
            count += 1
            print(f"{chr(i)}{chr(k)}{chr(j)}", end=" ")

print(count)