def opcionesMenu():
    print("1: Registro de piloto ")
    print("2: Eliminar piloto")
    print("3: Modificar puntos o tiempo promedio")
    print("4: Informe general")
    print("5: Salir")


def ingresar_opcionesMenu(desde, hasta):
    #Función realizada por Joaquin Olmedo
    #Función para verificar que la opción ingresada en el menu sea correcta

    op = int(input("Seleccione una opcion: "))
    while op<desde or op>hasta:
        print("La opcion seleccionada no es valida")
        op = int(input("Seleccione una opcion:"))
    return op

def ingresarPositivo(msg):
    #Función realizada por Joaquin Olmedo
    #Función para verificar que el valor sea positivo
    num=int(input(msg))
    while num<=0:
        print("Error debe ser positivo")
        num=int(input(msg))
    return num

def altadePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf):
    #da de alta alos pilotos hasta ingresar -1
    #Función realizada por Joaquin Olmedo

    
    nombre=input("Ingrese el nombre del piloto o -1 para finalizar: ")
        
        #Se solicita el numero del monoplaza
    monoplaza= int(input("Ingrese el numero del monoplaza:"))

        #Se solicita la escuderia
    escuderia = input("Ingrese la escuderia del piloto: ")

        #Se solicita la cantidad de puntos que tiene el piloto
    puntos = ingresarPositivo("Ingrese cantidad de puntos:")

        #Se solicita el tiepo de vuelta promedio
    vuelta = ingresarPositivo("Ingrese la vuelta promedio:")

        #Se solicita el presupuesto
    presupuesto = ingresarPositivo("Ingrese el presupuesto:")

        #Se solicita el numero abandonos
    dnf = ingresarPositivo("Ingrese cantidad de abandonos:")

     #guardar en las listas
    lst_nombres.append(nombre)
    lst_numero.append(monoplaza)
    lst_escuderia.append(escuderia)
    lst_puntos.append(puntos)
    lst_vueltaProm.append(vuelta)
    lst_presupuesto.append(presupuesto)
    lst_dnf.append(dnf)
    
    nombre = input("Ingrese el nombre del piloto: ")

def bajaDePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf):
    #Da de baja un piloto, posteriormente vuelve al menu, 
    #Función realizada por Juan Manuel

        #Se solicita el número de monoplaza
    monoplaza = int(input("Ingrese el número de monoplaza"))

    posicion = -1
    i= 0

    #Se busca al piloto dentro de la lista de números

    while i < len(lst_numero):
        if lst_numero[i] == monoplaza:
            posicion = i
        i = i + 1

    #En caso de no existir se notifica, y se revisa que este mismo tenga 0 puntos para poder ser eliminado  
    if posicion == -1:
        print("El piloto que esta buscando no existe")
    else:
        if lst_puntos[posicion] != 0:
            print("Para poder eleminarlo debe tener 0 puntos")
        else:
            print("El piloto a eliminar es:", lst_nombres[posicion])

            confirmacion = int(input("Desea confirmar la eliminación del piloto?, 1 si, 2 para cancelar"))
            #n caso de poder ser eliminado, se borran los datos de ese piloto de todas las listas.  
            if confirmacion == 1:
                lst_nombres.pop(posicion)
                lst_numero.pop(posicion)
                lst_escuderia.pop(posicion)
                lst_puntos.pop(posicion)
                lst_vueltaProm.pop(posicion)
                lst_presupuesto.pop(posicion)
                lst_dnf.pop(posicion)

                print("Se elmino al piloto")
            else:
                print("Se cancelo la eliminación")



def modificarPiloto(lst_nombres, lst_numero, lst_escuderia, lst_puntos, lst_vueltaProm, lst_presupuesto, lst_dnf):
    #Función hecha por Juan Manuel, permite modificar los puntos de un piloto, o su tiempo promedio, accediendo por nombre o número de monoplaza
    print("1: Buscar por nombre")
    print("2: Buscar por número de monoplaza")

    opcion = int(input("Elija una opción: "))

    posicion = -1

    if opcion == 1:
        nombre = input("Ingrese el nombre del piloto: ")
        i = 0
        while i < len(lst_nombres) and posicion == -1:
            if lst_nombres[i].upper() == nombre.upper():
                posicion = i
            i = i + 1
    elif opcion == 2:
        numero = int(input("Ingrese el número de monoplaza: "))
        i = 0
        while i < len(lst_numero) and posicion == -1:
            if lst_numero[i] == numero:
                posicion = i

            i = i + 1

    if posicion == -1:
        print("Piloto no encontrado")

    else:
        print("Piloto encontrado:", lst_nombres[posicion])
        print("1. Cambiar puntos")
        print("2. Cambiar tiempo promedio ")
        print("3. Cambiar ambos")

        opcionModificacion = int(input("Elija una opción:"))

        if opcionModificacion == 1:

            nuevosPuntos = int(input("Ingrese los nuevos puntos:"))
            lst_puntos[posicion] = nuevosPuntos

            print("Puntos modificados correctamente")
        elif opcionModificacion == 2:

            nuevoTiempo = float(input("Ingrese el nuevo tiempo promedio:"))
            lst_vueltaProm[posicion] = nuevoTiempo

            print("Tiempo promedio modificado")
        elif opcionModificacion == 3:

            nuevosPuntos = int(input("Ingrese los nuevos puntos: "))
            nuevoTiempo = float(input("Ingrese el nuevo tiempo promedio: "))

            lst_puntos[posicion] = nuevosPuntos
            lst_vueltaProm[posicion] = nuevoTiempo

            print("Datos modificados")
        else:
            print("Opción inválida")





def generarInforme(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf): 
        #Función que se encarga de realizar el informe usando las listas encontradas en el main, realizada por Juan Manuel

    #Para poder listarlas correctamente tengo que ordenarlas
    for i in range(len(lst_nombres)-1):
        for j in range(i+1, len(lst_nombres)):
            #Primero pide ordenar por en un orden decreciente por puntos
            if lst_puntos[i] < lst_puntos[j]:
                aux = lst_nombres[i]
                lst_nombres[i] = lst_nombres[j]
                lst_nombres[j] = aux

                aux = lst_numero[i]
                lst_numero[i] = lst_numero[j]
                lst_numero[j] = aux

                aux = lst_escuderia[i]
                lst_escuderia[i] = lst_escuderia[j]
                lst_escuderia[j] = aux

                aux = lst_puntos[i]
                lst_puntos[i] = lst_puntos[j]
                lst_puntos[j] = aux

                aux = lst_vueltaProm[i]
                lst_vueltaProm[i] = lst_vueltaProm[j]
                lst_vueltaProm[j] = aux

                aux = lst_presupuesto[i]
                lst_presupuesto[i] = lst_presupuesto[j]
                lst_presupuesto[j] = aux

                aux = lst_dnf[i]
                lst_dnf[i] = lst_dnf[j]
                lst_dnf[j] = aux

            # Después solicita, que en caso de empatar en puntos, se ordene por tiempo de vuelta creciente
            elif lst_puntos[i] == lst_puntos[j]:

                if lst_vueltaProm[i] > lst_vueltaProm[j]:

                    aux = lst_nombres[i]
                    lst_nombres[i] = lst_nombres[j]
                    lst_nombres[j] = aux

                    aux = lst_numero[i]
                    lst_numero[i] = lst_numero[j]
                    lst_numero[j] = aux

                    aux = lst_escuderia[i]
                    lst_escuderia[i] = lst_escuderia[j]
                    lst_escuderia[j] = aux

                    aux = lst_puntos[i]
                    lst_puntos[i] = lst_puntos[j]
                    lst_puntos[j] = aux

                    aux = lst_vueltaProm[i]
                    lst_vueltaProm[i] = lst_vueltaProm[j]
                    lst_vueltaProm[j] = aux

                    aux = lst_presupuesto[i]
                    lst_presupuesto[i] = lst_presupuesto[j]
                    lst_presupuesto[j] = aux

                    aux = lst_dnf[i]
                    lst_dnf[i] = lst_dnf[j]
                    lst_dnf[j] = aux
    
    print("---------INFORME PRINCIPAL---------")
    for i in range(len(lst_nombres)):
        print("Nombre del piloto", lst_nombres[i])
        
        print("Número de monoplaza del piloto", lst_numero[i])
        
        print("Escuderia del piloto", lst_escuderia[i])
        
        print("Puntos del piloto", lst_puntos[i])
        
        print("Tiempo promedio del piloto", lst_vueltaProm[i])

        print("Presupuesto del piloto", lst_presupuesto[i])   
            
        print("Cantidad de abandonos del piloto", lst_dnf[i])
    print("-----------------------------------")

    
    
