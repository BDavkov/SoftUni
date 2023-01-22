input_hour = int(input())
input_minutes = int(input())

minutes = (input_hour * 60) + input_minutes + 15

total_hour = minutes // 60
total_minutes = minutes % 60

if total_hour == 24:
    total_hour = 0

print(f"{total_hour}:{total_minutes:02d}")
