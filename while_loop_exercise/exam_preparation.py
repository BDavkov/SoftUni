failed_grades_count = int(input())
grades_count = 0
all_grades = 0
last_subject = ""
failed_grades = 0
flag = False
while True:
    subject_name = input()
    if subject_name == "Enough":
        flag = True
        break

    last_subject = subject_name

    current_grade = int(input())
    if current_grade <= 4:
        failed_grades += 1
        if failed_grades == failed_grades_count:
            break

    grades_count += 1
    all_grades += current_grade

avg_score = all_grades / grades_count
if flag:
    print(f"Average score: {avg_score:.2f}\nNumber of problems: {grades_count}\nLast problem: {last_subject}")
else:
    print(f"You need a break, {failed_grades} poor grades.")