e1 = int(input())
e2 = int(input())
s1 = int(input())
s2 = int(input())

exam_minutes = (e1 * 60) + e2
student_minutes = (s1 * 60) + s2
diff = abs(student_minutes - exam_minutes)

if student_minutes > exam_minutes:
    print("Late")
elif diff <= 30:
    print("On time")
elif diff > 30:
    print("Early")

hours = diff // 60
minutes = diff % 60

if exam_minutes > student_minutes:
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")
elif exam_minutes < student_minutes:
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")
