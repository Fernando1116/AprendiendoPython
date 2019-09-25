#Se pide al usuario que de un valor entre 1 al 9.
numero=input("Dame un numero del 1 al 9:")

#Se agrega el tipo de dato int ya que los numeros son enteros.
numero=int(numero)

#Se utiliza for para que ejecute un bloque de codigo varias veces.
#En range se utiliza un numero mas del necesario como se muestra en la linea 9.
for i in range(1,11):
    #i va cambiando en cada resultado.
    salida="{} x {} = {}"
    #Se muestra el resultado.
    print(salida.format(numero,i,i*numero))