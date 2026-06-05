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
