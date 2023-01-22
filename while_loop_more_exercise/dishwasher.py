detergent = int(input())
detergent_count = detergent * 750
counter = 0
dishes = 0
pots = 0
flag = False

while True:
    counter += 1
    things = input()
    if things == "End":
        flag = True
        break
    else:
        things = int(things)
        if counter % 3 == 0:
            pots += things
            detergent_count -= (things * 15)
        else:
            dishes += things
            detergent_count -= (things * 5)

        if detergent_count < 0:
            break

if flag:
    print(f"Detergent was enough!\n{dishes} dishes and {pots} pots were washed.\nLeftover "
          f"detergent {detergent_count} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_count)} ml. more necessary!")
