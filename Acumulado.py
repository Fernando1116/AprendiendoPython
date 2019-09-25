#Se declara la variable con tipo entero
acumulado=int(0)

#Se declara la variable con tipo str
numero=str("")

#Se utiliza el while para que un a partir de ahi sea un ciclo infinito hasta que se
#utilice un break.
#En este caso True tiene la condicion de while el ciclo sera infinito hasta que se utilice break.
while True:
   #Se pide un numero.
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si el usuario no reporto nada se rompe el ciclo y sale del programa.
        print("Vacio. Salida del programa.")
        break
    else:
        #Si el usuario reporto un numero entonces, acumulado=acumulado+numero
        #A continuacion se realiza la operacion.
        acumulado+=int(numero)
        #Se da la instruccion de como aparecera en la pantalla.
        salida="Monto acumulado: {}"
        #Se imprime el resultado.
        print(salida.format(acumulado))