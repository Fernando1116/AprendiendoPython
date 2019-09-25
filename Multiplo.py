#Se pide un numero, una vez dado, se convertira en int y se guardara.
numero=int(input("Dame un numero: "))

#Se almacenan los valores, despues de que se hayan hecho las evaluaciones con sus resoectivos residuales.
#Si es cero el residual significa es que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

#and= Se utiliza si todas las condiciones son verdaderas.
#or= Se utiliza si al menos una condicion es verdadera.
#El parentesis que esta dentro de un parentesis "(())" significa que las condiciones son juntas,
#y el tercer parentesis es independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")