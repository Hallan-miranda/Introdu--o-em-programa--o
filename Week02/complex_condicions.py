gpa = float(input('whats was your grade point avereange? '))
lowest_grade = float(input('Whats your lowers grade? '))

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('You made the honour roll')

# if gpa >= .85 and lowest_grade >= .70:
#     print('You made the honour roll')

if gpa >= .85 and lowest_grade >= .70:
    honour_fall = True
else:
    honour_fall = False

if honour_fall:
    print('You made honour roll')