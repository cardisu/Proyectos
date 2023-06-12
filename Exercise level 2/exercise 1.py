"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

n=input("Ingrese un numero: \n")
name=input("Ingrese su nombre: \n")
print("La repeticion es:")
for i in range(int(n)):
    print(name)

