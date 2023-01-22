juniors_count = int(input())
seniors_count = int(input())
trace = input()

tax_juniors = 0
tax_seniors = 0
all_tax = 0
all_count = juniors_count + seniors_count

if trace == "trail":
    tax_juniors = 5.5 * juniors_count
    tax_seniors = 7 * seniors_count
    all_tax = tax_seniors + tax_juniors
elif trace == "cross-country":
    tax_juniors = juniors_count * 8
    tax_seniors = seniors_count * 9.5
    if all_count >= 50:
        all_tax = (tax_seniors + tax_juniors) * 0.75
    else:
        all_tax = tax_seniors + tax_juniors
elif trace == "downhill":
    tax_juniors = juniors_count * 12.25
    tax_seniors = seniors_count * 13.75
    all_tax = tax_seniors + tax_juniors
elif trace == "road":
    tax_juniors = juniors_count * 20
    tax_seniors = seniors_count * 21.5
    all_tax = tax_seniors + tax_juniors

tax_with_expenses = all_tax * 0.95

print(f"{tax_with_expenses:.2f}")
