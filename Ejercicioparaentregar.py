#Un programa que arroje una lista de numeros que pida cuantos numeros tendrá al usuario, arroje la lista de numeros aleatorios, los sume y genere una nueva lista con los pares o impares
import random

listaDeNumero = []
cantidadDeNumeros : int = int(input("Cuantos numeros quieres que tenga tu lista entre 1 y 100:")) 
for adicionarNumero in range(cantidadDeNumeros):
    listaDeNumero.append(random.randint(0,100))

print(listaDeNumero)

sumadeNumero = 0
for numero in listaDeNumero:
    sumadeNumero = sumadeNumero + numero
    
print(sumadeNumero)

listadePares = []
listadeImpares = []
for numero in listaDeNumero:
    if numero == 0 or numero % 2 == 0:
        listadePares.append(numero)
    else:
        listadeImpares.append(numero)
        
print(listadePares)
print(listadeImpares)
    