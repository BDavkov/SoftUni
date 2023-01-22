racer1 = int(input())
racer2 = int(input())
racer3 = int(input())

total_seconds = racer2 + racer3 + racer1
total_minutes = total_seconds // 60
total_seconds_left = total_seconds % 60

print(f"{total_minutes}:{total_seconds_left:02d}")
