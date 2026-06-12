from Funciones import *

def main():

    lst_nombres=["Max Verstappen", "Charles Leclerc", "Lando Norris", "Franco Colapinto" ]
    lst_numero=[3, 16, 1, 43]
    lst_escuderia=["RedBull", "Ferrari", "McLaren", "Alpine"]
    lst_puntos=[125, 80, 62, 110]
    lst_vueltaProm=[78.45, 82.62, 88.23, 79.35]
    lst_presupuesto=[2000000.20, 1800000, 1700000.98, 1530000.88 ]
    lst_dnf=[0, 2, 1, 3]
    
    opcionesMenu()
    opciones = ingresar_opcionesMenu(1, 5)

    while opciones != 5:
        if opciones == 1:
            print("Registro de piloto")
            altadePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf)

        elif opciones == 2:
            print("Eliminar piloto")
            bajaDePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf)
       
        elif opciones == 3:
            print("Modificar tiempo promedio o puntos")
            modificarPiloto(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf)
         
        elif opciones == 4:
            print("Informe general")
            generarInforme(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf)
        
        elif opciones == 5:
            print("Salir")
        
        opcionesMenu()
        opciones = ingresar_opcionesMenu(1,5)       
main()
