number = float(input())

if number // 2 == 0 and number % 10 == 0.5:
    print(number + 0.5)
else:
    print(round(number))