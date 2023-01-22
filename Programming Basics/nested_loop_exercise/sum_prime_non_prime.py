prime = 0
non_prime = 0

while True:
    current_number = input()
    if current_number == "stop":
        break

    number = int(current_number)
    count = 0
    if number < 0:
        print("Number is negative.")
        continue

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count <= 2:
        prime += number
    else:
        non_prime += number

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
