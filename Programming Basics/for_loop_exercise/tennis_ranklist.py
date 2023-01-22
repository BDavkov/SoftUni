tournaments_count = int(input())
start_points = int(input())

wins = 0
final_points = start_points
for i in range(1, tournaments_count + 1):
    position = input()
    if position == "W":
        final_points += 2000
        wins += 1
    elif position == "F":
        final_points += 1200
    elif position == "SF":
        final_points += 720

print(f"Final points: {final_points}")

average_points = (final_points - start_points) // tournaments_count

print(f"Average points: {average_points}")

percent_of_wins = (wins / tournaments_count) * 100

print(f"{percent_of_wins:.2f}%")
