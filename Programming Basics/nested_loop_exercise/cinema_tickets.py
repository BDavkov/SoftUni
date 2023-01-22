student_count = 0
standard_count = 0
kids_count = 0
total = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    current_tickets = 0

    tickets = int(input())
    for i in range(1, tickets + 1):
        type_ticket = input()

        if type_ticket == "End":
            break

        current_tickets += 1
        total += 1

        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        elif type_ticket == "kid":
            kids_count += 1

        if current_tickets == tickets:
            break

    print(f"{movie_name} - {(current_tickets / tickets) * 100:.2f}% full.")

print(f"Total tickets: {total}")
print(f"{(student_count / total) * 100:.2f}% student tickets.")
print(f"{(standard_count / total) * 100:.2f}% standard tickets.")
print(f"{(kids_count / total) * 100:.2f}% kids tickets.")
