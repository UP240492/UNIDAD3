#EJERCICIOS DEL NIVEL 1

#EJERCICIO 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Encontrar la longitud del conjunto it_companies
print(f"Length of it_companies: {len(it_companies)}")

#EJERCICIO 2
it_companies.add('Twitter')
print(f"it_companies after adding Twitter: {it_companies}")

#EJERCICIO 3 
rrr = {'Netflix', 'Tesla', 'Spotify'}
it_companies.update(rrr)
print(f"it_companies after adding multiple companies: {it_companies}")

#EJERCICIO 4
it_companies.remove('Google')
print(f"it_companies after removing Google: {it_companies}")

#EJERCICIO 5
# El método remove() generará un error KeyError si el elemento no existe en el conjunto.
# El método discard() no generará un error si el elemento no existe en el conjunto.

# Ejemplo de remove
try:
    it_companies.remove('NonExistentCompany')
except KeyError:
    print("Tried to remove a non-existent company using remove() and caught a KeyError.")

# Ejemplo de discard
it_companies.discard('NonExistentCompany')
print("Tried to discard a non-existent company using discard() without any error.")

#EJERCICIOs DEL NIVEL 2

#EJERCICIO 1
A = {19, 22, 24}
B = {19, 22, 20}
A_union_B = A.union(B)
print(f"A union B: {A_union_B}")

#EJERCICIO 2
A_intersection_B = A.intersection(B)
print(f"A intersection B: {A_intersection_B}")

#EJERCICIO 3
is_A_subset_of_B = A.issubset(B)
print(f"Is A a subset of B? {is_A_subset_of_B}")

#EJERCICIO 4
are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets? {are_disjoint}")

#EJERCICIO 5
A_union_B = A.union(B)
B_union_A = B.union(A)
print(f"A union B: {A_union_B}")
print(f"B union A: {B_union_A}")

#EJERCICIO 6
A_symmetric_difference_B = A.symmetric_difference(B)
print(f"A symmetric difference B: {A_symmetric_difference_B}")

#EJERCICIO 7
del A
del B

#EJERCICIOS DEL NIVEL 3

#EJERCICIO 1
ages = [22, 19, 24]
ages_set = set(ages)
list_length = len(ages)
set_length = len(ages_set)

#EJERCICIO 2
ages = [22, 19, 24]
ages_set = set(ages)
list_length = len(ages)
set_length = len(ages_set)

print(f"Length of the list: {list_length}")
print(f"Length of the set: {set_length}")

if list_length > set_length:
    print("The list is bigger.")
elif list_length < set_length:
    print("The set is bigger.")

#EJERCICIO 3
oracion = "I am a teacher and I love to inspire and teach people"
words = oracion.split()
dfdf= set(words)
print(f"Unique words: {dfdf}")
print(f"Number of unique words: {len(dfdf)}")




