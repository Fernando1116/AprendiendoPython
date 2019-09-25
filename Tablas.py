for i  in range(1,11):
    encabezado="Tabla del {}"
    #Cuando se quiere saltar una linea se utiliza print sin ningun argumento.
    print()
    #Se agregara un for dentro del for principal
    for j in range(1,11):
        #En este punto la variable i contiene la base de la tabla.
        #Y j el elemento de la misma.
        salida="{} x {} = {}"
        #Aqui se muestra el procedimiento de la multiplicacion.
        print(salida.format(i,j,i*j))
    else:
            #Al concluir se las multiplicaciones indicadas, se ejecuta el codigo,
            #que es un salto de linea con print.
            print()