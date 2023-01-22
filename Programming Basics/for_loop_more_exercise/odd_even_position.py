import sys

numbers = int(input())

even_min = sys.maxsize
even_max = -sys.maxsize
even_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
odd_sum = 0
for i in range(1, numbers + 1):
    current_number = float(input())
    if i % 2 == 0:
        even_sum += current_number
        if even_max < current_number:
            even_max = current_number
        if even_min > current_number:
            even_min = current_number
    else:
        odd_sum += current_number
        if odd_max < current_number:
            odd_max = current_number
        if odd_min > current_number:
            odd_min = current_number

if numbers == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif numbers == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
