first_match = input()
second_match = input()
third_match = input()

won, lost, drawn = 0, 0, 0

if first_match[0] > first_match[2]:
    won += 1
elif first_match[0] == first_match[2]:
    drawn += 1
else:
    lost += 1

if second_match[0] > second_match[2]:
    won += 1
elif second_match[0] == second_match[2]:
    drawn += 1
else:
    lost += 1

if third_match[0] > third_match[2]:
    won += 1
elif third_match[0] == third_match[2]:
    drawn += 1
else:
    lost += 1

print(f"Team won {won} games.\nTeam lost {lost} games.\nDrawn games: {drawn}")
