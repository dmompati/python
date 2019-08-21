name = input('Enter your name ')
age = int(input('Enter you age '))

if age > 30:
    print(name, 'is at level', age)
elif age < 30:
    print(name, 'is', age, 'years old')
else:
    print(name,'is', age)