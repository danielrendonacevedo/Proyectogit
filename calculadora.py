#Definir una función que permita imprimar la tabla de multiplicar, pero esta función debe recibir la tabla a operar y el operador. La función que realicen debe poder ejecutar cualquier operación
operadorUsuario= str(input("Escribe un operador: + - * / "))
numeroUsuario1= int(input("Escribe un primer numero cualquiera: "))
numeroUsuario2 = int(input("Escribe un segundo numero cualquiera: "))

def tablaDemultiplicar (num):
    tablaMultiplicar = []
    for i in range(1, 11):
        if num == 0:
            print("No hay tabla del 0")
            break
        else:
            numeroAdicionarAtabla = (num * i)
            tablaMultiplicar.append(numeroAdicionarAtabla)
            i = i+1
    print (f" La tabla de multiplicar hasta 10 del primer numero es : {tablaMultiplicar}")

def calculadora (numero1, numero2, operador):
    if type(numero1) != int or type(numero2) != int:
        print("No ingresaste un número")
    else:
        if operador == "+":
            suma: int = numero1 + numero2 
            print(f" La suma de los dos numeros da: {suma}") 
        elif operador == "-":
            resta: int = numero1 - numero2
            print(f" La resta de los dos numeros da: {resta}")
        elif operador == "*":
            multiplicacion: int = numero1 * numero2
            print(f" La multiplicación de los dos numeros da: {multiplicacion}")
        elif operador == "/":
            if numeroUsuario1 == 0 or numeroUsuario2 == 0:
                print("No es posible la división por cero")
            else:
                division: int = numero1 / numero2
                print(f" La Divisón de los dos numeros da: {division}")
        else:
            print("No es un operador válido")
        
calculadora(numeroUsuario1, numeroUsuario2, operadorUsuario)
tablaDemultiplicar(numeroUsuario1)
    
        
        
    