#El usuario nos dara una respuesta y la respuesta tendra la variable de "nombre"
nombre=input("Nombre:")
apellidos=input("Apellidos:")

#Se enlazaran los valores junto con la literal ("")
nombreCompleto=nombre+ " " +apellidos

#Ya enlazado el nombre y apellido se pide convertirlos en mayusculas para eso se utilizara .upper()
nombreCompleto=nombreCompleto.upper()

#Se imprime el resultado
print(nombreCompleto)