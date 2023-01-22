cargo_count = int(input())

all_cargo = 0
van_count = 0
truck_count = 0
train_count = 0
for i in range(1, cargo_count + 1):
    current_cargo = int(input())
    all_cargo += current_cargo
    if current_cargo <= 3:
        van_count += current_cargo
    elif current_cargo <= 11:
        truck_count += current_cargo
    else:
        train_count += current_cargo

van = 200 * van_count
truck = 175 * truck_count
train = 120 * train_count

avg_cargo = (van + truck + train) / all_cargo
print(f"{avg_cargo:.2f}")
print(f"{van_count / all_cargo * 100:.2f}%")
print(f"{truck_count / all_cargo * 100:.2f}%")
print(f"{train_count / all_cargo * 100:.2f}%")