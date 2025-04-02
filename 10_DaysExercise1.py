#NIVEL 1
#EJERCICIO 1
print("Using for loop:")
for i in range(11):
    print(i)

print("Using while loop:")
i = 0

#EJERCICIO 2
print("Using for loop (10 to 0):")
for i in range(10, -1, -1):
    print(i)

print("Using while loop (10 to 0):")
i = 10
while i >= 0:
    print(i)
    i -= 1

#EJERCICIO 3
for i in range(1, 11):
    print('#'*i)

#EJERCICIO 4
for i in range(11):
    for j in range(11):
        print('#', end=' ')
    print()

#EJERCICIO 5
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#EJERCICIO 6
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in technologies:
    print(tech)

#EJERCICIO 7
print("Even numbers from 0 to 100:")
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#EJERCICIO 8
print("Odd numbers from 0 to 100:")
for i in range(0, 101):
    if i % 2 != 0:
        print(i)

#EJERCICIOS NIVEL 2
#EJERCICIO 1
print("Sum of all numbers from 0 to 100:")
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}.")

#EJERCICIO 2
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is {sum_evens}.")
print(f"The sum of all odds is {sum_odds}.")

#EJERCICIOS NIVEL 3
#EJERCICIO 1
from data.countries import countries # type: ignore
# Extraer países que contienen la palabra 'land'
countries_with_land = [country for country in countries if 'land' in country]
print("Countries containing 'land':")
print(countries_with_land)

#EJERCICIO 2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

# Usar un bucle para invertir el orden
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruit list:")
print(reversed_fruits)

#EJERCICIO 3
from data.countries_data import countries_data  # type: ignore # Asegúrate de que el archivo countries_data.py esté en la carpeta data

# Total de idiomas en los datos
languages = set()
for country in countries_data:
    languages.update(country['languages'])
print(f"Total number of languages: {len(languages)}")

# Diez idiomas más hablados
language_count = {}
for country in countries_data:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1

most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTen most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

# Diez países más poblados
most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("\nTen most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

ountries_data = [
    {
        "name": "Afghanistan",
        "population": 38928346,
        "languages": ["Pashto", "Uzbek", "Turkmen"]
    },
    {
        "name": "Albania",
        "population": 2877797,
        "languages": ["Albanian"]
    },
    # Más países...
]


