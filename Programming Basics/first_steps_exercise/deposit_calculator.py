deposit_sum = float(input())
term = int(input())
interest = float(input())
final_sum = deposit_sum + term * ((deposit_sum * (interest / 100)) / 12)

print(final_sum)