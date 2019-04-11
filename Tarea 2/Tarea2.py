#Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista
print("********** Parte 1 de la tarea **********")
lista_de_valores = [5, 6, 10, 13, 3, 4, 15, 7, 16, 8]
print("La cantidad de valores en la lista llamada lista_de_valores es:", len(lista_de_valores))
indice = len(lista_de_valores)
#i = 0
total2 = 0
for i in range(indice):
    total = lista_de_valores[i]
    total2 = total + total2

promedio = total2 / indice
print("El promedio de la lista es:", promedio)

print()
print()
print("**********Parte dos de la tarea**********")
#Determinar el grupo que tiene la mayor altura
todos = [
[177,145,167,190,140,150,180,130], # grupo 1
[165,176,145,189,170,189,159,190], # grupo 2
[145,136,178,200,123,145,145,134], # grupo 3
[201,110,187,175,156,165,156,135] # grupo 4
]
a = 1
#Creo la lista que van a contener la suma total de cada sublistas dentro la lista todos
suma_de_grupo_total = []
for a in range(len(todos)):
    print(todos[a], end=" ")
    suma_de_grupo = sum(todos[a])
    suma_de_grupo_total.append(suma_de_grupo)
#   variable para incrementar el numero del group
    grupo = a + 1
    print("La suma del grupo %i es: %i" % (grupo,suma_de_grupo))

#La suma los numeros de cada sublista en la lista llamada todos
print("La suma de cada subrupo es ", suma_de_grupo_total[:])
#Imprime los numeros salvados en la nueva lista
print("La cantidad de indices en la lista que contiene las sumatorias es:" , (len(suma_de_grupo_total)))
#Imprime el numero mas alto de la nueva lista donde se guardo la sumatoria de todos los numeros de cada group

print("El grupo", suma_de_grupo_total.index(max(suma_de_grupo_total))+1, "es el que tiene la mayor altura.")
