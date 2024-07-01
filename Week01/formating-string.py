first_name = input('Wahts your fist name ')
last_name = input('Wahts your last name ')

#output = 'Hello ' + first_name + ' ' + last_name
#output = 'Hello, {} {}'.format(first_name, last_name)
#output = 'Hello, {1} {0}'.format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
print(output.title())