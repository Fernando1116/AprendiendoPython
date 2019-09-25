#Existen librerias en Python, y para que se puedan utilizar tenemos que primero importarla 
#utilizando import
import random

#Se utiliza una variable tipo float y se dara un valor.
#El tipo float se utiliza para numeros decimales.
numero1=float(10.5)

#En esta linea se utilizaran las funciones para ejecutar la tarea.
#Def se utiliza para que todo lo que este dentro forme parte de la funcion.
def miFuncion():
    #El numero que sea generado se convertira en float utilizando el random.randrange().
    numero2=float(random.randrange(1,10))
    #
    #Se sustituyen para el resultado.
    mensaje="La suma de {} y {} es {}"
    #
    #Se suman los numeros que se generaron.
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Y por ultimo se ejecuta la funcion.
miFuncion()