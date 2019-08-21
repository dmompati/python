def numbers(x,y):
    
    if x > y:
        return x
    else:
        return y

print(numbers(6,3))

def morenumbers(x):
    if x > 5:
        return True
    else:
        return False

print(morenumbers(4))

def extranumbers(x):
    if x == "hayley is awesome":
        return True
    else:
        return False

print(extranumbers('hayley is awesomes'))

def names(name,age):
    if age > 30:
        return name + ' is at level ' + age
    elif age < 30:
        return name + ' is ' + age + 'years old'

print(names('dessie', 22))