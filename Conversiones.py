#Se utiliza la variable str ya que es una cadena y la utilizaremos en los digitos.
#Se utiliza str cuando se hara una cadena.
numero="1234"

#Aqui se muestra el tipo que utiliza la variable.
print(type(numero))

#Aqui se convierte a entero usando int.
#int se utiliza para numeros enteros.
numero=int(numero)

#Se vuelve a mostrar el tipo de variable que se utiliza, pero ahora con el cambio.
print(type(numero))

#Se manda un mensaje en donde los {} son en donde pondran el resultado.
salida="El numero utilizado es {}"

#Por ultimo se imprime el resultado.
print(salida.format(numero))