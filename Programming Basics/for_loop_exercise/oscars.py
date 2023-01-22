actor_name = input()
academy_points = float(input())
count_evaluative = int(input())

all_points = academy_points
for i in range(1, count_evaluative + 1):
    name = input()
    points = float(input())
    all_points += (len(name) * points) / 2
    if all_points > 1250.5:
        break

if all_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    diff = abs(1250.5 - all_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
