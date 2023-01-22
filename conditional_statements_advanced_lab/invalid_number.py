num = int(input())
is_valid = 0

if 100 <= num <= 200 or num == 0:
    is_valid = True

if not is_valid:
    print("invalid")
