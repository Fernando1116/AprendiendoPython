#Se utilizara una variable para que el usuario de un valor.
#input se utiliza para dar un valor externo o sea mediante el usuario.
entrada=input()

#Se identifica el tipo de dato.
print(type(entrada))

#El valor booleano verificara si lo capturado es digito, si no llegase a encontrar un punto
#significara que se trata de un numero decimal, eso quiere decir que es float.
#Si find se devuelve -1 quiere decir que lo busco \, en este caso no se encontro.
#Si esEntero es verdadero, lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #En esta linea se ejecuta la condicion True
    print("Dato entero. ¡Muy bien!")
else:
    #Y en esta linea se ejecuta la condicion false.
    print("Dato no es entero. Intentar nuevamente")