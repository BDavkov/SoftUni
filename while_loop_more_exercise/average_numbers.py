number = int(input())
counter = 0
sum_numbers = 0
while counter < number:
    counter += 1
    current_number = int(input())
    sum_numbers += current_number

avg_sum = sum_numbers / number

print(f"{avg_sum:.2f}")
