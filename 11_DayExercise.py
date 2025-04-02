# EJERCICIO 1
def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(3, 5)
print(f"The sum is: {result}")

#EJERCICIO 2
import math

def area_of_circle(r):
    return math.pi * r * r

# Ejemplo de uso
radius = 5
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")

#EJERCICIO 3
def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "All arguments must be numbers."
        total += arg
    return total

print(add_all_nums(1, 2, 3, 4))  # Salida: 10
print(add_all_nums(1, 'a', 3))   # Salida: All arguments must be numbers.

#EJERCICIO 4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = 25
fahrenheit_temp = convert_celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

#EJERCICIO 5
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

month = "March"
season = check_season(month)
print(f"The season in {month} is {season}.")

#EJERCICIO 6
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "The slope is undefined (vertical line)."
    slope = (y2 - y1) / (x2 - x1)
    return slope

x1, y1 = 2, 3
x2, y2 = 5, 11
slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is {slope}.")

#EJERCICIO 7
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c  # Calcular el discriminante
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real roots"

# Ejemplo de uso
a, b, c = 1, -3, 2  # Coeficientes de la ecuación x² - 3x + 2 = 0
solutions = solve_quadratic_eqn(a, b, c)
print(f"The solutions of the quadratic equation are: {solutions}")

#EJERCICIO 8
def print_list(items):
    for item in items:
        print(item)

sample_list = [1, 2, 3, 4, 5]
print("Elements of the list:")
print_list(sample_list)

#EJERCICIO 9
def reverse_list(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array

sample_list = [1, 2, 3, 4, 5]
reversed_sample = reverse_list(sample_list)
print(f"Original list: {sample_list}")
print(f"Reversed list: {reversed_sample}")

#EJERCICIO 10
def capitalize_list_items(items):
    capitalized_items = [item.capitalize() for item in items]
    return capitalized_items

sample_list = ['apple', 'banana', 'cherry']
capitalized_list = capitalize_list_items(sample_list)
print(f"Original list: {sample_list}")
print(f"Capitalized list: {capitalized_list}")

#EJERCICIO 11
def add_item(lst, item):
    lst.append(item)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]

#EJERCICIO 12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#EJERCICIO 13
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_of_numbers(5))   # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100)) # 5050

#EJERCICIO 14
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # Verificar si el número es impar
            total += i
    return total

print(sum_of_odds(5))   # 9 (1 + 3 + 5)
print(sum_of_odds(10))  # 25 (1 + 3 + 5 + 7 + 9)
print(sum_of_odds(100)) # 2500

#EJERCICIO 15
def sum_of_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # Verificar si el número es par
            total += i
    return total

print(sum_of_even(5))   # 6 (2 + 4)
print(sum_of_even(10))  # 30 (2 + 4 + 6 + 8 + 10)
print(sum_of_even(100)) # 2550

#NIVEL 2
#EJERCICIO 1
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))

#EJERCICIO 2
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ejemplo de uso
print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(10)) # 3628800

#EJERCICIO 3
def is_empty(param):
    return not bool(param)

# Ejemplo de uso
print(is_empty([]))       # True (la lista está vacía)
print(is_empty({}))       # True (el diccionario está vacío)
print(is_empty(""))       # True (la cadena está vacía)
print(is_empty([1, 2]))   # False (la lista no está vacía)
print(is_empty("Hello"))  # False (la cadena no está vacía)

#EJERCICIO 4
def calculate_mean(lst):
    return sum(lst) / len(lst)

# Función para calcular la mediana
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
    # Función para calcular la moda
def calculate_mode(lst):
    from collections import Counter
    freq = Counter(lst)
    max_count = max(freq.values())
    modes = [key for key, count in freq.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]

# Función para calcular el rango
def calculate_range(lst):
    return max(lst) - min(lst)

# Función para calcular la varianza
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

# Función para calcular la desviación estándar
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print(f"Mean: {calculate_mean(data)}")          # Media
print(f"Median: {calculate_median(data)}")      # Mediana
print(f"Mode: {calculate_mode(data)}")          # Moda
print(f"Range: {calculate_range(data)}")        # Rango
print(f"Variance: {calculate_variance(data)}")  # Varianza
print(f"Std Dev: {calculate_std(data)}")        # Desviación estándar

#NIVEL 3
#EJERCICIO 1
def is_prime(number):
    if number <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(number ** 0.5) + 1):  # Verificar divisores hasta la raíz cuadrada del número
        if number % i == 0:
            return False
    return True

# Ejemplo de uso
print(is_prime(2))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(20))  # False
print(is_prime(29))  # True

#EJERCICIO 2
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))

# Ejemplo de uso
print(are_all_items_unique([1, 2, 3, 4, 5]))  # True (todos los elementos son únicos)
print(are_all_items_unique([1, 2, 2, 4, 5]))  # False (hay elementos duplicados)

#EJERCICIO 3
def are_all_items_same_type(lst):
    if not lst:  # Verificar si la lista está vacía
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)


print(are_all_items_same_type([1, 2, 3, 4]))       # True (todos son enteros)
print(are_all_items_same_type(['a', 'b', 'c']))    # True (todos son cadenas)
print(are_all_items_same_type([1, 'a', 3.5]))      # False (diferentes tipos)
print(are_all_items_same_type([]))                 # True (lista vacía)

#EJERCICIO 4
def is_valid_variable(var): # type: ignore
    return var.isidentifier()


print(is_valid_variable("variable1"))  # True (válido)
print(is_valid_variable("1variable"))  # False (no puede comenzar con un número)
print(is_valid_variable("var!able"))   # False (contiene un carácter no permitido)
print(is_valid_variable("_variable"))  # True (válido)
print(is_valid_variable("while"))      # True (válido, pero es una palabra reservada)

#EJERCICIO 5
from data.countries_data import countries_data  # type: ignore # Asegúrate de que el archivo countries_data.py esté en la carpeta data

Imprimir los nombres de todos los países # type: ignore
for country in countries_data:
    print(country['name'])

from collections import Counter

def most_spoken_languages(countries_data, top_n=10):
    language_count = Counter()
    for country in countries_data:
        for language in country['languages']:
            language_count[language] += 1
    return language_count.most_common(top_n)

def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

print("Most spoken languages:")
for language, count in most_spoken_languages(countries_data, 10):
    print(f"{language}: {count}")

print("\nMost populated countries:")
for country in most_populated_countries(countries_data, 10):
    print(f"{country['name']}: {country['population']}")

    

