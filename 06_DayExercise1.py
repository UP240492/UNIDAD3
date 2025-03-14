#EJERCICIOS DEL NIVEL 1

#EJERCICIO 1
empty_tuple = ()
print(empty_tuple)

#EJERCICIO 2
siblings = ('Juan', 'Maria', 'Pedro')
print(siblings)     

#EJERCICIO 3
brothers = ('Juan', 'Pedro')
sisters = ('Maria',)            
siblings = brothers + sisters
print(siblings) 

#EJERCICIO 4
num_siblings = len(siblings)
print(f"Tengo{num_siblings} hermanos.")

#EJERCICIO 5
father = ('Carlos',)
mother = ('Ana',)
family_members = siblings + father + mother
print(family_members)

#EJERCICIOS DEL NIVEL 2

#EJERCICIO 1
siblings = family_members[:-2]
parents = family_members[-2:]
print(f"Siblings: {siblings}")
print(f"Parents: {parents}")

#EJERCICIO 2
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#EJERCICIO 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#EJERCICIO 4
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print(middle_items)

#EJERCICIO 5
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")

#EJERCIO 6
del food_stuff_tp

#EJERCICIO 7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"Is Estonia a nordic country? {is_estonia_nordic}")

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(f"Is Iceland a nordic country? {is_iceland_nordic}")

