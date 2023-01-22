n1 = int(input())
n2 = int(input())
operator = input()

red_flag = False

result = 0
if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 == 0:
        red_flag = True
    else:
        result = n1 / n2
elif operator == "%":
    if n2 == 0:
        red_flag = True
    else:
        result = n1 % n2

even_odd = ""
if result % 2 == 0:
    even_odd = "even"
elif result % 2 == 1:
    even_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {even_odd}")
elif operator == "/":
    if red_flag:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if red_flag:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {result}")
