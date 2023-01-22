fuel = input()
liters = float(input())
card = input()

gasoline_price = liters * 2.22
diesel_price = liters * 2.33
gas_price = liters * 0.93

if card == "Yes":
    gasoline_price -= liters * 0.18
    diesel_price -= liters * 0.12
    gas_price -= liters * 0.08

if liters > 25:
    gasoline_price *= 0.9
    diesel_price *= 0.9
    gas_price *= 0.9
elif 20 <= liters <= 25:
    gasoline_price *= 0.92
    diesel_price *= 0.92
    gas_price *= 0.92

if fuel == "Gasoline":
    print(f"{gasoline_price:.2f} lv.")
elif fuel == "Diesel":
    print(f"{diesel_price:.2f} lv.")
elif fuel == "Gas":
    print(f"{gas_price:.2f} lv.")
