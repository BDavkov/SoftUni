n = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
divides = 0

points = 0
for n in range(n):
    color = input()
    if color == "red":
        points += 5
        red_balls += 1
    elif color == "orange":
        points += 10
        orange_balls += 1
    elif color == "yellow":
        points += 15
        yellow_balls += 1
    elif color == "white":
        points += 20
        white_balls += 1
    elif color == "black":
        points //= 2
        divides += 1
    else:
        other_colors += 1

print(f"Total points: {int(points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {divides}")