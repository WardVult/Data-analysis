professions = ['Engineer', 'Doctor', 'Teacher', 'Artist', 'Scientist']
sports = ['Football', 'Basketball', 'Tennis', 'Baseball', 'Swimming']
family_members = ['Mother', 'Father', 'Brother', 'Sister']

print(professions)
print(sports)
print(family_members)

sorted_professions = sorted(professions)
print("sorted professions:", sorted_professions)

sports.reverse()
print("reverse sports", sports)

family_string = ', '.join(family_members)
print("family members", family_string)