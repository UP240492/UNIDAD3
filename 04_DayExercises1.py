#EJERCICIO 1
WORD1, WORD2, WORD3, WORD4 = 'THIRTY', 'DAYS', 'OF', 'PYTHON'
SINGLE_STRING = WORD1 + ''+ WORD2 + '' + WORD3 + '' + WORD4 
print('La oracion es:',SINGLE_STRING)

#EJERCICIO 2
word1, word2, word3 = 'Coding', 'For', 'All'
single_strings = word1 + word2 + word3
print('la oracion es:',single_strings)

#EJERCICIO 3
empresa = 'Coding for all'

#EJERCICIO 4
print(empresa)

#Ejercicio 5
print('ejercicio 5')
print(len(empresa))

#EJERCICIO 6
palabra = 'empresa'
word = palabra.upper()
print(word)

#EJERCICIO 7
palabra = 'EMPRESA'
word_b = palabra.lower()
print(word_b)

#EJERCICIO 8
word_c = 'Dios te ama'
print(word_c.capitalize())
print(word_c.title())
print(word_c.swapcase())

#EJERCICIO 9
empresa= 'Coding For All'
palabra = empresa.replace('Coding','')
print(palabra)

#EJERCICIO 10
if empresa.find('Coding') == 0:
    print(True)
else:
    print(False)

#EJERCICIO 11
replaceWord = empresa.replace("Coding" , "Python")
print(replaceWord)

#EJERCICIO 12
palabra1 = 'PYTHON FOR EVERYONE'
palabra2 = palabra1.replace('PYTHON FOR ALL','')
print(palabra2)

#EJERCICIO 13
print('ejercicio 13')
print(palabra1.split())

#EJERCICIO 14
print('ejercicio 14')
wxw = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
p1q = wxw.split()
print(p1q)

#EJERCICIO 15
print('ejercicio 15')
ww = empresa[0]
print(ww)

#EJERCICIO 16
print('ejercicio 16')
zz = empresa[-1]
print(zz)

#EJERCICIO 17
print('ejercicio 17')
xx = empresa[10]
print(xx)

#EJERCICIO 18 
print('ejercicio 18')
rrr = "Python for everyone"
acronimo = "".join(word[0] for word in rrr.split())
print(acronimo)

#EJERCICIO 19
print('ejercicio 19')
eee = 'Coding for all'
acronimo2 = "".join(word[0] for word in eee.split())
print(acronimo2)

#EJERCICIO 2O
print('ejercicio 20')
ttt = 'Coding For All'
print(ttt.find('C'))

#EJERCICIO 21
print('ejecicio 21')
print(ttt.find('F'))

#EJERCICIO 22
print('ejercicio 22')
print(ttt.find('l'))

#EJERCICIO 23
jjj = 'You cannot end a sentence with because because because is a conjunction'
print(jjj.find('because'))

#EJERCICIO 24
qqq = jjj.find("You")
print(qqq)

#EJERCICIO 25
print('ejercicio 25')
uuu = jjj[27:50]
print(uuu)

#EJERCICIO 26
print('ejercicio 26')
kkk = jjj.find('because')
print(kkk)

#EJERCICIO 27
sentence = 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because because because')
end_index = start_index + len('because because because')
sliced_sentence = sentence[:start_index] + sentence[end_index:]
print(sliced_sentence)

#EJERCICIO 28
eee = 'Coding For All'
if eee.find == 0:
    print('Si esta')
else:
    print('NO ESTA')

#EJERCICIO 29
if eee.find == 1:
    print('si esta')
else:
    print('no esta')

#EJERCICIO 30
oracion = 'Coding For All'
sss = "".join(oracion.split())
print(sss)

#EJERCICIO 31
var1 = '30DaysOfPython'
print(var1.isidentifier())#False
var2 = 'Thirty_days_of_python'
print(var2.isidentifier())#True
#la funcion isidentifier checa si puede o no ser un nombre valido para crear la variable

#EJERCICIO 32
librerys= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
result = "#".join(librerys)
print(result)

#EJERCICIO 33
separar = 'I am enjoying this challenge.\nI just wonder what is next'
print(separar)

#EJERCICIO 34

tabular = "Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\t\Helsinki"
print(tabular)

#EJERCICIO 35
radius = 10
area = 3.14 * radius ** 2
fomatear = f"The area of a circle with radius {radius} is {area} meters square"
print(fomatear)

#EJERCICIO 36
formateo = f"las operacionesaritmeticas de 8 y 6 son suma de {8+6},\n su recta es {8-6}, la multiplicacion de \n{8*6}, su {8//6} y potencia de {8**6}"
print(formateo)




