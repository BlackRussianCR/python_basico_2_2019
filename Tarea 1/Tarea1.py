#Valor de Pi
pi = 3.1415926
#Imprime el valor de Pi
print(pi)
#Determina el length de Pi y lo imprime. Tambien le resta 1, para no contar el estacio del punto (".")
Pi_Real=(len(str(pi)) - 1)
print("El length de Pi es:", Pi_Real)
#Inicializo el contador para el while
i = 1;
while i <= Pi_Real:
    #Utilizo el end = '' para indicarle al loop de while que tiene que imprimir en una sola linea
    print(("%s %.{}f".format(Pi_Real - i) % ("*" * i, pi)), end = ' ')
    i = i + 1;