#NIVEL 1
#EJERCICIO 1
import random
def random_user_id(variable):
     variable = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
     return variable
print(random_user_id(""))
 
 
#EJERCICIO 2
def user_id_gen_by_user(VAriable2):
     num_chars = int(input("Ingrese el número de caracteres: "))
     num_ids = int(input("Ingrese el número de IDs a generar: "))
     VAriable2= [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=num_chars)) for _ in range(num_ids)]
     return(VAriable2)
print(user_id_gen_by_user(""))
 
#EJERCICIO 3
def rgb_color_gen(var3):
     var3 = f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"
     return var3
print(rgb_color_gen(0))
 
#NIVEL 2
#EJERCICIOS 1
def list_of_hexa_colors(n):
     return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]
print(list_of_hexa_colors(4))
 
#EJERCICIO 2
def list_of_rgb_colors(n):
     var4 = [rgb_color_gen() for _ in range(n)]
 
#EJERCICIO 3
def generador_colores(color_type, n):
     if color_type == 'hexa':
         return list(n)
     elif color_type == 'rgb':
         return list_of_rgb_colors(n)
     else:
         return "Color no valido"
print(generador_colores("",2))
 
#NIVEL 3
#EJERCICIO 1
def shuffle_list(lst):
     random.shuffle(lst)
     return lst
print(shuffle_list(["Hola", "Piña", "bazinga"]))
 
#EJERCICIO 2
def unique_random_numbers():
     randomizado = random.sample(range(10), 7)
     return randomizado
print(unique_random_numbers)