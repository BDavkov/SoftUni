people = int(input())
total = 0
grades = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    all_grades = 0
    for i in range(1, people + 1):
        current_grade = float(input())
        all_grades += current_grade
        total += current_grade
        grades += 1

    print(f"{presentation} - {all_grades / people:.2f}.")

print(f"Student's final assessment is {total / grades:.2f}." )