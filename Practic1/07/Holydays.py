days = int(input("Enter the number of holiday days: "))

total_hours = days * 24
total_minutes = total_hours * 60
total_seconds = total_minutes * 60

print("{:<10} : {}".format("Hours", total_hours))
print("{:<10} : {}".format("Minutes", total_minutes))
print("{:<10} : {}".format("Seconds", total_seconds))