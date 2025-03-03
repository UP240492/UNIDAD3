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
lado3 = int(input(ingrese el tercer lado))
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
q1, z1, q2, z2 = 1, 0, -2
FirstSlope = (z2 - z1) / (q2 - q1)
print("The slope is  ", FirstSlope)

# ejercicio 9
x1, y1, x2, y2 = 2,2,6,10
Second_Slope = (y2 - y1) / (x2 - x1)
print("The slope is" ,Second_Slope)
euclidean_distance = math.sqrt((x2 - x1) **2 + (y2-y1) ** 2)
print("la distancia eucladiana es ", euclidean_distance)

# ejericio 10
if (First_slope == Second_Slope):
    print('son iguales')
else : print('no son iguales, estas mal')

# ejercicio 11
x = int(input "ingrese el valor de x")
y = int(y=x^2 + 6*x + 9)
print("el valor de y es, y")

# ejercicio 12
palabra1 = len("python")
palabra2 = len("dragon")
if(palabra1 != palabra2):
    print("es diferente largo")
else: "tiene la misma longitud"

