#EJERCICIO 1
lista_vacia = []

#EJERCICIO 2
lista = [1,2,3,4,5,6,7]

#EJERCICIO 3
longitud = len(lista)
print(longitud)

#EJERCICIO 4
primer_elemento = lista[0]
enmedio = lista[len(lista)//2]
ultimo = lista[-1]
print(primer_elemento)
print(enmedio)
print(ultimo)

#EJERCICIO 5
mixed_data_types = ['david',18,1.72,'soltero','aguascalientes']

#EJERCICIO 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#EJERCICIO 7
print(it_companies)

#EJERCICIO 8
print(len(it_companies))

#EJERCICIO 9
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print(first_company)
print(middle_company)
print(last_company)

#EJERCICIO 10
it_companies[0] = it_companies[0].upper()
print(it_companies)

#EJERCICIO 11
it_companies.append('Twitter')  
print(it_companies) 

#EJERCICIO 12
middle_company = it_companies[len(it_companies)//2]
it_companies.insert(middle_company,'LinkedIn')
print(it_companies)

#EJERCICIO 13
it_companies[1] = it_companies[1].upper() #changing 'google' to uppercase
print(it_companies)

#EJERCICIO 14
join_companies = '#;'.join(it_companies)  
print(join_companies)

#EJERCICIO 15
company_to_ceck = 'Facebook'
if company_to_ceck in it_companies:
    print(f"{company_to_ceck} exists in the list.")
else:
    print(f"{company_to_ceck} does not exist in the list.")

#EJERCICIO 16
it_companies.sort()
print(it_companies)

#EJERCICIO 17
it_companies.reverse()
print(it_companies)

#EJERCICIO 18
first_three = it_companies[:3]
print(first_three)

#EJERCICIO 19
last_three_companies = it_companies[-3:]                
print(last_three_companies)

#EJERCICIO 20
middle_index = len(it_companies)//2
if len(it_companies)%2 != 0:
    middle_company = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_company = [it_companies[middle_index]]
print(middle_company)

#EJERCICIO 21
it_companies.pop(0) 
print(it_companies)

#EJERCICIO 22
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    # Remove two middle companies
    it_companies.pop(middle_index)
    it_companies.pop(middle_index - 1)
else:
    # Remove the single middle company
    it_companies.pop(middle_index)
print(it_companies)

#EJERCICIO 23
it_companies.pop()  
print(it_companies)

#EJERCICIO 24
it_companies.clear()    
print(it_companies)

#EJERCICIO 25
del it_companies

#EJERCICIO 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#EJERCICIO 27
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

#EJERCICIO NIVEL 2
# LIST OF STUDENTS
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(f"Ages after adding min and max again: {ages}")

# 3. Find the median age (one middle item or two middle items divided by two)
ages.sort()
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print(f"Median age: {median_age}")

# 4. Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# 5. Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f"Age range: {age_range}")

# 6. Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print(f"Min - Average: {min_average_diff}")
print(f"Max - Average: {max_average_diff}")

# List of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 1. Find the middle country(ies) in the countries list
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print(f"Middle country(ies): {middle_countries}")

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half
if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

# 3. Unpack the first three countries and the rest as scandic countries
first, second, third, *scandic_countries = countries
print(f"First country: {first}")
print(f"Second country: {second}")
print(f"Third country: {third}")
print(f"Scandic countries: {scandic_countries}")

