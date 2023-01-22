number1 = int(input())
number2 = int(input())

for number in range(number1, number2 + 1):
    number_in_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_in_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=" ")
