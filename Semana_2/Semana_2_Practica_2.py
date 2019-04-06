#Crear un codigo que calcule las soluciones de la ecuacion cuadratica

import math

print("Digite los siguiente valores")

a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))

x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2 * a)

x2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2 * a)

print(x1)
print(x2)