lenght = int(input())
width = int(input())
volume = lenght * width
flag = False

while True:
    current_cakes = input()
    if current_cakes == "STOP":
        flag = True
        break
    else:
        current_cakes = int(current_cakes)
        volume -= current_cakes
        if volume <= 0:
            break

if flag:
    print(f"{volume} pieces are left." )
else:
    print(f"No more cake left! You need {abs(volume)} pieces more.")
