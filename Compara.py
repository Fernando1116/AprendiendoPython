#Se le pide al usuario que de valor a dos variables.
numero1=input("Numero 1:")
numero2=input("Numero 2:")

#Se muestra cuales son los numeros dados.
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #Se imprimira un mensaje si la funcion de if se cumple.
    #En este caso si la variable 1 y 2 son iguales se imprimira que son iguales.
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    #Si en dado caso los numeros son diferentes se abre otro if
    if numero1>numero2:
        #Si se cumple la funcion, se imprimira que el primer numero es mayor que el segundo.
        print(salida.format(numero1, numero2,"El mayor es el primero"))
    else:
            #Si no se cumple la funcion se imprimira que el segundo numero es mayor que el primero.
            print(salida.format(numero1, numero2,"Ël mayor es el segundo"))