#EJERCICIO 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)  # [-4, -3, -2, -1, 0]

#EJERCICIO 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist in list_of_lists for inner_list in sublist for number in inner_list]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#EJERCICIO 3
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)

# Salida:
# [(0, 1, 0, 0, 0, 0, 0),
#  (1, 1, 1, 1, 1, 1, 1),
#  (2, 1, 2, 4, 8, 16, 32),
#  (3, 1, 3, 9, 27, 81, 243),
#  (4, 1, 4, 16, 64, 256, 1024),
#  (5, 1, 5, 25, 125, 625, 3125),
#  (6, 1, 6, 36, 216, 1296, 7776),
#  (7, 1, 7, 49, 343, 2401, 16807),
#  (8, 1, 8, 64, 512, 4096, 32768),
#  (9, 1, 9, 81, 729, 6561, 59049),
#  (10, 1, 10, 100, 1000, 10000, 100000)]

#EJERCICIO 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] 
                       for sublist in countries for country in sublist]
print(flattened_countries)

# Salida:
# [['FINLAND', 'FIN', 'HELSINKI'], 
#  ['SWEDEN', 'SWE', 'STOCKHOLM'], 
#  ['NORWAY', 'NOR', 'OSLO']]

#EJERCICIO 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict_list = [{'country': country[0].upper(), 'city': country[1].upper()} 
                       for sublist in countries for country in sublist]
print(countries_dict_list)

# Salida:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
#  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#  {'country': 'NORWAY', 'city': 'OSLO'}]

#EJERCICIO 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{name[0]} {name[1]}" for sublist in names for name in sublist]
print(concatenated_names)

# Salida:
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
