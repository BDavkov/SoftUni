groups = int(input())
all_count = 0
Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0
for i in range(1, groups + 1):
    group_count = int(input())
    all_count += group_count
    if group_count <= 5:
        Musala += group_count
    elif group_count <= 12:
        Monblan += group_count
    elif group_count <= 25:
        Kilimandjaro += group_count
    elif group_count <= 40:
        K2 += group_count
    else:
        Everest += group_count

Musala_percent = (Musala / all_count) * 100
Monblan_percent = (Monblan / all_count) * 100
Kilimandjaro_percent = (Kilimandjaro / all_count) * 100
K2_percent = (K2 / all_count) * 100
Everest_percent = (Everest / all_count) * 100

print(f"{Musala_percent:.2f}%")
print(f"{Monblan_percent:.2f}%")
print(f"{Kilimandjaro_percent:.2f}%")
print(f"{K2_percent:.2f}%")
print(f"{Everest_percent:.2f}%")
