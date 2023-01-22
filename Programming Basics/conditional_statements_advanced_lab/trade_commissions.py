town, sell = input(), float(input())
commission = 0

if town == "Sofia":
    if 0 <= sell <= 500:
        commission = 0.05
    elif 500 < sell <= 1000:
        commission = 0.07
    elif 1000 < sell <= 10000:
        commission = 0.08
    elif sell > 10000:
        commission = 0.12
elif town == "Varna":
    if 0 <= sell <= 500:
        commission = 0.045
    elif 500 < sell <= 1000:
        commission = 0.075
    elif 1000 < sell <= 10000:
        commission = 0.1
    elif sell > 10000:
        commission = 0.13
elif town == "Plovdiv":
    if 0 <= sell <= 500:
        commission = 0.055
    elif 500 < sell <= 1000:
        commission = 0.08
    elif 1000 < sell <= 10000:
        commission = 0.12
    elif sell > 10000:
        commission = 0.145

price = commission * sell

if town == "Sofia" or town == "Varna" or town == "Plovdiv" and sell >= 0:
    print(f"{price:.2f}")
else:
    print("error")
