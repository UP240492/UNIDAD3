edad = 18
altura = 1.71

complejo = 1+1j
base = int(input('enter base: '))
height = int(input('enter height: '))
area = int(0.5*base*altura)
print('el area es de:', area)

#numero 5
lado1 = int(input('ingresa la longitud de un lado'))
lado2 = int(input('ingrese el segundo lado'))
lado3 = int(input("ingrese el tercer lado"))
perimetro = lado1 + lado2 + lado3
print('el perimetroes de:',perimetro)

#area y perimetro de un rectangulo
l1 = int(input('ingrese la altura del rectangulo'))
l2 = int(input('ingrese la base del rectangulo'))
Area = l1*l2
Perimetro = 2*(l1+l2)
print('el area del rectangulo es de:', area)
print('el perimetro del recatngulo es:', perimetro)

#circulo numero 7
radio = int(input('ingresa el radio del circulo'))
pi= 3.14
area =pi*radio*radio
circunferencia = 2*pi*radio
print('el area del circulo es de:', area)
print('la circunferencia del circulo es de:',circunferencia)

# ejercicio 8
# z = 2q - 2 q = x z = y 
q1, z1, q2, z2 = 2,2,6,10
FirstSlope = (z2 - z1) / (q2 - q1)
print("The slope is  ", FirstSlope)

# ejercicio 9
x1, y1, x2, y2 = 2,2,6,10
Second_Slope = (y2 - y1) / (x2 - x1)
print("The slope is" ,Second_Slope)
euclidean_distance = ((x2 - x1) **2 + (y2-y1) ** 2)
print("la distancia eucladiana es ", euclidean_distance)


# ejericio 10
if ("First_slope == Second_Slope"):
    print('son iguales')
else : print('no son iguales, estas mal')

# ejercicio 11
x = input ("ingrese el valor de x")
y = int(y=x^2 + 6*x + 9)
print("el valor de y es, y")

# ejercicio 12
palabra1 = len("python")
palabra2 = len("dragon")
if(palabra1 != palabra2):
    print("es diferente largo")
else: "tiene la misma longitud"

#ejercicio 13
print('on' in 'python' and 'on'in 'dragon') # output: true

#ejercicio 14
print("jargon" in  "i hope this course is not full of jargon")

#ejercicio 15
print("no" in "dragon" and "no" in "python")

#ejercicio 16
pythonLen = len("python")
print(float(pythonLen))
print(int(pythonLen))

#ejercicio 17
number = float(input("put a nomber"))
reminder = number % 2
if(reminder == 0):
    print("the number is divisible for 2")
else: print("the number is not divisible for 2")

#ejercicio 18
division = 7//3
resultado = 2.7 
if division == resultado:
    print('Si es igual')
else: print('No es igual a 2.7, es igual a:',division)

#ejercicio 19
comprar = type(10)
if comprar == 10:
    print('Si es igual a 10')
else: print('no es igual a 10')

#ejercicio 20
valor = int(9.8)

if valor == 10:
    print('El valor de 9.8 si es igual a 10')

else:('El valor de 9.8 no es igual a 10')

#ejercicio 21
horas = int(input('ingresa las horas laborables'))
pago_por_hora = int(input('Ingresa el sueldo por hora'))
sueldo_total = horas*pago_por_hora
print('Su sueldo total es de:',sueldo_total)

#ejercicio 22
años = int(input('ingresa los años vividos'))
total = años*3600*24*364
print('El total de sgundos vividos es:',total)

#ejercicio 23
print('ejercicio 23')

for i in range (1,6):
    print( i, 1, i**2, i**2, 1**3)
    

