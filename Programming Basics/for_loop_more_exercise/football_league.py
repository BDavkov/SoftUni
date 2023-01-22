stadium_capacity = int(input())
fans_count = int(input())

A, B, V, G = 0, 0, 0, 0
for i in range(1, fans_count + 1):
    current_sector = input()
    if current_sector == "A":
        A += 1
    elif current_sector == "B":
        B += 1
    elif current_sector == "V":
        V += 1
    elif current_sector == "G":
        G += 1

a_percent = A / fans_count * 100
b_percent = B / fans_count * 100
v_percent = V / fans_count * 100
g_percent = G / fans_count * 100

print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{fans_count / stadium_capacity * 100:.2f}%")
