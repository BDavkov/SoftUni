import math
import sys

numbers = int(input())
a = 0
diff1 = -sys.maxsize

max_sum = -sys.maxsize
min_sum = sys.maxsize
for i in range(1, numbers + 1):
    sum1 = a
    num1 = int(input())
    num2 = int(input())
    sum2 = num1 + num2

    if i != 1:
        if abs(sum2 - sum1) > diff1:
            diff1 = abs(sum2 - sum1)

    if (num1 + num2) > max_sum:
        max_sum = num1 + num2
    if (num1 + num2) < min_sum:
        min_sum = num1 + num2

    a = num1 + num2

if max_sum == min_sum:
    print(f"Yes, value={max_sum}")
else:
    print(f"No, maxdiff={diff1:.0f}")
