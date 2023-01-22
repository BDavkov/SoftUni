world_record = float(input())
meteres_distance = float(input())
seconds_duration = float(input())

how_long = meteres_distance * seconds_duration
lag = (meteres_distance // 15) * 12.5
total = how_long + lag

if total < world_record:
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    print(f"No, he failed! He was {total - world_record:.2f} seconds slower.")