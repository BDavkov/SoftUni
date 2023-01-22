import math
import sys

numbers = int(input())

max_sum = -sys.maxsize
min_sum = sys.maxsize
for i in range(1, numbers + 1):
    num1 = int(input())
    num2 = int(input())
    if (num1 + num2) > max_sum:
        max_sum = num1 + num2
    if (num1 + num2) < min_sum:
        min_sum = num1 + num2

diff = math.dist((max_sum,), (min_sum,))
if max_sum == min_sum:
    print(f"Yes, value={max_sum}")
else:
    print(f"No, maxdiff={diff:.0f}")
