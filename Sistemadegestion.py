from Funciones import *

def main():
    
    opcionesMenu()
    opciones = ingresar_opcionesMenu(1, 8)

    while opciones != 8:
        if opciones == 1:
            print("Registro de piloto")

        elif opciones == 2:
            print("Eliminar piloto")

        elif opciones == 3:
            print("modificar puntos")
            
        elif opciones == 4:
            print("Modificar tiempo promedio")
            
        elif opciones == 5:
            print("Informe general")
        
        elif opciones == 6:
            print("Salir")
        
        opcionesMenu()
        opciones = ingresar_opcionesMenu(1,8)       
main()