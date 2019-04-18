#Tarea 3 listas

#Parte 1
print("")
print("")
print("Parte 1 de la tarea")
print("")
lista_palabras_1 = []
palabras_1 = int(input("Digite la cantidad de palabras que va a ingresar: "))
x = 0
y = 1
while x <= (palabras_1 - 1):
    palabra_1 = str(input("Digite la palabra %i: " % (y)))
    lista_palabras_1.append(palabra_1)
    y = y + 1
    x = x + 1

print("La lista de palabras ingresadas son:", lista_palabras_1[:])
print("Usted a ingresado un total de", len(lista_palabras_1), "palabras en la lista")

#Parte 2
#Para acortar codigo, estare usando la misma lista creada en la parte 1
print("")
print("")
print("Parte 2 de la tarea")
print("")
buscar = str(input("Cual palabra desea buscar en la lista?: "))

if buscar in lista_palabras_1:
    print("La palabra", buscar, "se repite", lista_palabras_1.count(buscar), "veces.")
else:
    print("La palabra", buscar, "no existe en la lista")

#Parte 3
#Para acortar codigo, estare usando la misma lista creada en la parte 1
print("")
print("")
print("Parte 3 de la tarea")
print("")
print("La lista tiene actualmente las siguientes palabras")
print(lista_palabras_1)
reemplazar = str(input("Digite la palabra que quiere reemplazar: "))
if reemplazar in lista_palabras_1:
    reemplazado = str(input("Digite la nueva palabra: "))
    n = 0
    for n in range(len(lista_palabras_1)):
       if reemplazar == lista_palabras_1[n]:
            lista_palabras_1[n] = reemplazado
       n = n + 1
else:
    print("La palabra ", reemplazar, "no existe en la lista")
print("")
print("La lista tiene actualmente las siguientes palabras")
print(lista_palabras_1)

#Parte 4
#Para acortar codigo, estare usando la misma lista creada en la parte 1
print("")
print("")
print("Parte 4 de la tarea")
print("")
borrar = str(input("Digite la palabra que quiere borrar: "))
print("")
if borrar in lista_palabras_1:
    while (lista_palabras_1.count(borrar)):
        lista_palabras_1.remove(borrar)
    print("La lista fue modificada y contiene las siguientes palabras: ", lista_palabras_1[:])
else:
    print("La palabra a borrar no existe")

#Parte 5
#Para acortar codigo, estare usando la misma lista creada en la parte 1
print("")
print("")
print("Parte 5 de la tarea")
print("")
print("La lista original tiene las siguiente palabras: ", lista_palabras_1[:])
lista_palabras_5 = []
palabras_5 = int(input("Digite cuantas palabras tiene la lista de palabras a eliminar: "))
x = 0
y = 1
while x <= (palabras_5 - 1):
    palabra_5 = str(input("Digite la palabra numero %i: " % (y)))
    lista_palabras_5.append(palabra_5)
    x = x + 1
    y = y + 1
print("La segunda lista creada contiene las siguientes palabras: ", lista_palabras_5[:])
print("")
print("Todas las palabras que se repiten tanto en la lista 1, como en la lista 2 van a ser borradas")
nueva_lista = list((set(lista_palabras_1)) - set(lista_palabras_5))
print("Hora la lista contiene las siguientes palabras: ", nueva_lista[:])

#Parte 6
print("")
print("")
print("Parte 6 de la tarea")
print("Este ejercicio lo que hace es invertir el orden de palabras de la lista en un lista nueva")
print("")
lista_palabras_1 = []
palabras_1 = int(input("Digite la cantidad de palabras que va a ingresar: "))
x = 0
y = 1
while x <= (palabras_1 - 1):
    palabra_1 = str(input("Digite la palabra %i: " % (y)))
    lista_palabras_1.append(palabra_1)
    y = y + 1
    x = x + 1
largo = len(lista_palabras_1)
indice = largo - 1
lista_nueva = []
x = 1
for x in range(largo):
    while indice != -1:
        palabra = lista_palabras_1[indice]
        lista_nueva.append(palabra)
        indice = indice - 1
    x = x + 1
print("")
print("La lista original contiene las palabras en el siguiente orden")
print(lista_palabras_1)
print("")
print("La lista invertida ahora es:")
print(lista_nueva)
print("")

#Parte 7
print("")
print("")
print("Parte 7 de la tarea")
print("")
print("Este ejercicio va a eliminar las palabras duplicada, dejando en la lista solo una palabra de ellas")
print("")
lista_palabras_1 = []
palabras_1 = int(input("Digite la cantidad de palabras que va a ingresar: "))
x = 0
y = 1
while x <= (palabras_1 - 1):
    palabra_1 = str(input("Digite la palabra %i: " % (y)))
    lista_palabras_1.append(palabra_1)
    y = y + 1
    x = x + 1
lista_nueva = []
lista_nueva = list(set(lista_palabras_1))
print("")
print("La lista original contiene las palabras")
print(lista_palabras_1[:])
print("")
print("La lista sin palabras repetidas es:")
print(lista_nueva[:])

#Parte 8
print("")
print("")
print("Parte 8 de la tarea")
print("")
print("")
print("Este ejercicio va a realizar las siguiente actividades")
print("Mostrar palabras que aparecen en ambas listas")
print("Mostrar palabras que solo aparecen en la primera lista")
print("Mostrar palabras que solo aparecen en la segunda lista")
print("Mostrar todas las palabras que aparecen en ambas listas")
print("")
lista_palabras_1 = []
palabras_1 = int(input("Digite la cantidad de palabras que va a ingresar: "))
x = 0
y = 1
while x <= (palabras_1 - 1):
    palabra_1 = str(input("Digite la palabra %i: " % (y)))
    lista_palabras_1.append(palabra_1)
    y = y + 1
    x = x + 1
lista_palabras_1 = list(set(lista_palabras_1))

lista_palabras_2 = []
palabras_2 = int(input("Digite la cantidad de palabras que va a ingresar: "))
x = 0
y = 1
while x <= (palabras_2 - 1):
    palabra_2 = str(input("Digite la palabra %i: " % (y)))
    lista_palabras_2.append(palabra_2)
    y = y + 1
    x = x + 1
lista_palabras_2 = list(set(lista_palabras_2))

palabras_repeticas = list(set(lista_palabras_1) & set(lista_palabras_2))
print("Las palabras que aparecen en ambas listas son: ", palabras_repeticas[:])
print("")

palabras_unicas_lista_1 = list(set(lista_palabras_1) - set(lista_palabras_2))
print("Palabras unicas en la primera lista son: ", palabras_unicas_lista_1)
print("")

palabras_unicas_lista_2 = list(set(lista_palabras_2) - set(lista_palabras_1))
print("Palabras unicas en la segunda lista son: ", palabras_unicas_lista_2)
print("")

total_de_palabras = lista_palabras_1 + lista_palabras_2
print("Ambas listas contienen las siguientes palabras: ", total_de_palabras)