attendance = [18, 20, 19, 15, 21]

full_days = 0

for students in attendance:
    if students >= 20:
        print("Full")
        full_days += 1 
    else:
        print("Not Full")

print("Number of full days:", full_days)

total_attendance = sum(attendance)
print("Total attendance for 5 days:", total_attendance)
