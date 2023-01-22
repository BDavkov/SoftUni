name = input()
years = 1
total_grades = 0
failed_grades = 0

while years <= 12:
    years += 1
    grade = float(input())
    if grade >= 4:
        total_grades += grade
    else:
        failed_grades += 1
        years -= 1

    if failed_grades >= 2:
        print(f"{name} has been excluded at {years} grade")
        break

if years >= 12:
    print(f"{name} graduated. Average grade: {total_grades / 12:.2f}")
