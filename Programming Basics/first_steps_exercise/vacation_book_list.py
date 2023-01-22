number_of_pages = int(input())
pages_for_one_hour = int(input())
days = int(input())

how_long = number_of_pages / pages_for_one_hour
result = how_long / days

print(int(result))