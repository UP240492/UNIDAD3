#EJERCICIO 1
dog = {}
print (dog)

#EJERCICIO 2
dog['name'] =  'kira'
dog['color'] = 'black'
dog['breed'] = 'labrador'
dog['legs'] = 4
dog['age'] = 3
print (dog)

#EJERCICIO 3
student = {
    'first_name': 'Juan',
    'last_name': 'Perez',
    'gender': 'Man',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['gym', 'cars', 'soccer'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Av. Aguascalientes Sur',
    }
print (student)

#EJERCICIO 4
student_length = len(student)
print(f"Length of the student dictionary: {student_length}")

#EJERCICIO 5
skills = student['skills']
print(f"Skills: {skills}")
print(f"Data type of skills: {type(skills)}")

#EJERCICIO 6
student['skills'].append('programming')
student['skills'].append('public speaking')
print(f"Updated skills: {student['skills']}")

#EJERCICIO 7
student_keys = list(student.keys())
print(f"Dictionary keys: {student_keys}")

#EJERCICIO 8
student_values = list(student.values())
print(f"Dictionary values: {student_values}")

#EJERCICIO 9
student_items = list(student.items())
print(f"Dictionary as a list of tuples: {student_items}")

#EJERCICIO 10
# Usando del
del student['age']
print(f"Dictionary after deleting 'age': {student}")

# Usando pop()
removed_item = student.pop('address')
print(f"Dictionary after popping 'address': {student}")
print(f"Removed item: {removed_item}")

#EJERCICIO 11
del dog
print("Dictionary 'dog' has been deleted.")
 

