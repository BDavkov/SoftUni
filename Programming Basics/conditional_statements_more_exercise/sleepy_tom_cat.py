rest_days = int(input())

rest_days_minutes = rest_days * 127
working_days_minutes = (365 - rest_days) * 63
total_minutes = rest_days_minutes + working_days_minutes

diff = abs(30000 - total_minutes)
hours = diff // 60
minutes = diff % 60

if total_minutes > 30000:
    print(f"Tom will run away\n{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
