days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days + 1):
    current_patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if doctors >= current_patients:
        treated_patients += current_patients
    else:
        untreated_patients += current_patients - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
