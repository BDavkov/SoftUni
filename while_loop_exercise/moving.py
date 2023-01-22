width = int(input())
lenght = int(input())
height = int(input())
volume = width * lenght * height
flag = False

while True:
    current_boxes = input()
    if current_boxes == "Done":
        flag = True
        break
    else:
        current_boxes = int(current_boxes)
        volume -= current_boxes
        if volume <= 0:
            break

if flag:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
