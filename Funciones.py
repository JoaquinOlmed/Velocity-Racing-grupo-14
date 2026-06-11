def opcionesMenu():
    print("1: Registro de piloto ")
    print("2: Eliminar piloto")
    print("3: Modificar puntos")
    print("4: Tiempo promedio")
    print("5: Informe general")
    print("6: Salir")


def ingresar_opcionesMenu(desde, hasta):
    op = int(input("Selecicone una opcion: "))
    while op<desde or op>hasta:
        print("La opcion seleccionada no es valida")
        op = int(input("Selecicone una opcion:"))
    return op

def ingresarPositivo(msg):
    num=int(input(msg))
    while num<=0:
        print("Error debe ser positivo")
        num=int(input(msg))
    return num

def altadePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf):
    #da de alta alos pilotos hasta ingresar -1
    
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