"""
Christian Alonso Flores Burgos

Fecha
19 de septiembre de 2025

Dados tres números ordenarlos de mayor a menor.

"""

# Declaraciones
# Entradas
num1=int(input("Primer número:"))
num2=int(input("Segundo número:"))
num3=int(input("Tercer número:"))
# Proceso
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2

elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1

else: 
     mayor = num3
     if num1 >= num2:
        medio = num1
        menor = num2    
     else:
        medio = num2
        menor = num1
# Salidas
print("Números ordenados:",mayor, medio, menor)
