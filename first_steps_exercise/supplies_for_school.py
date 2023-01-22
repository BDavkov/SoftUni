pen = int(input())
marker =  int(input())
preparation = int(input())
discount = int(input())

pen_sum = pen * 5.8
marker_sum = marker * 7.2
preparation_sum = preparation * 1.2

final_sum = pen_sum + preparation_sum + marker_sum
needed_sum = final_sum - (final_sum * (discount / 100))

print(needed_sum)