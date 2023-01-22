budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250 * gpu_count
cpu_price = (0.35 * gpu_price) * cpu_count
ram_price = (0.1 * gpu_price) * ram_count
total = gpu_price + cpu_price + ram_price

if gpu_count > cpu_count:
    total -= 0.15 * total

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
