#NIVEL 1
#EJERCICIO 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - age
    print(f"You need {years_to_wait} more years to learn to drive.")

#EJERCICIO 2
my_age = 18
your_age = int(input("Enter your age: "))

# Comparar las edades
if your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
else:
    print("We are the same age.")

#EJERCICIO 3
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} and {b} are equal.")

#NIVEL 2
#EJERCICIO 1
score = int(input("Enter the students score: "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
        grade = "F"
else:
    grade = "Invalid score"

print(f"The students grade is {grade}.")

#EJERCICIO 2
month = input("Enter the month: ").capitalize()

if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season is: {season}")

#NIVEL 3
#EJERCICIO 1
persona = {
    'first_name': 'Juan',
    'last_name': 'Perez',
    'age': 30,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB'],
    'address': {
        'street': 'Calle 13',
        'zipcode': '12345'
    }
}

if 'skills' in persona:
    skills = persona['skills']

    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")

    if 'python' in skills:
        print("the person has python skill")
    else:
        print("the person does not have python skill")

    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer.")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
else:
    print("The person does not have skills.")


if persona['is_marred'] and persona['country'] == 'mexico':
    print(f"{persona['first_name']} {persona['last_name']} lives in {persona['country']}. He is married.")






