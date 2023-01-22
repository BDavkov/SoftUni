number_of_tabs = int(input())
in_salary = int(input())

salary = in_salary
for i in range(1, number_of_tabs + 1):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)
