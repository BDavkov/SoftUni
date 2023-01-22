budget = float(input())
ticket = input()
people_count = int(input())
transport_tax = 0
tickets_price = 0

if people_count <= 4:
    transport_tax = 0.75 * budget
elif 4 < people_count <= 9:
    transport_tax = 0.6 * budget
elif 9 < people_count <= 24:
    transport_tax = 0.5 * budget
elif 24 < people_count <= 49:
    transport_tax = 0.4 * budget
else:
    transport_tax = 0.25 * budget

if ticket == "VIP":
    tickets_price = people_count * 499.99
elif ticket == "Normal":
    tickets_price = people_count * 249.99

budget_after_tax = budget - transport_tax

if budget_after_tax >= tickets_price:
    print(f"Yes! You have {budget_after_tax - tickets_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {tickets_price - budget_after_tax:.2f} leva.")
