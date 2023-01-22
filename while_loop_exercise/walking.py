total_steps = 0
flag = False
while True:
    current_steps = input()
    if current_steps == "Going home":
        flag = True
        break
    current_steps = int(current_steps)
    total_steps += current_steps
    if total_steps >= 10000:
        break

if flag:
    more_steps = int(input())
    total_steps += more_steps
    if total_steps >= 10000:
        print(f"Goal reached! Good job!\n{total_steps - 10000} steps over the goal!")
    else:
        print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n{total_steps - 10000} steps over the goal!")
