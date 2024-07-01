print('The ')
grade_procent = float(input('What your grade procent? '))
letter = ''
sign = ''

last_digt = grade_procent %10

if last_digt >= 7:
    sign = "+"
elif last_digt < 3:
    sign = "-"
else:
    sign= ""

if grade_procent >= 90:
    letter = 'A'
elif grade_procent >= 80:
    letter = 'B'
elif grade_procent >= 70:
    letter = 'C'
elif grade_procent >= 60:
    letter = 'D'
else:
    letter = 'F'
    sign = " "
print('Your grade note is ' + letter + sign)

if grade_procent >= 70:
    print('Congratulations you passed the class!🥳')
else:
    print('You got close, continue to study and you will get the next time!😄')