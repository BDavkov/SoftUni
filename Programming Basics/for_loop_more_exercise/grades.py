student_count = int(input())
all_grades = 0
fail_student_count = 0
average_student_count = 0
good_student_count = 0
top_student_count = 0

for i in range(1, student_count + 1):
    current_grade = float(input())
    all_grades += current_grade
    if current_grade <= 2.99:
        fail_student_count += 1
    elif current_grade <= 3.99:
        average_student_count += 1
    elif current_grade <= 4.99:
        good_student_count += 1
    else:
        top_student_count += 1

print(f"Top students: {top_student_count / student_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good_student_count / student_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {average_student_count / student_count * 100:.2f}%")
print(f"Fail: {fail_student_count / student_count * 100:.2f}%")
print(f"Average: {all_grades / student_count:.2f}")
