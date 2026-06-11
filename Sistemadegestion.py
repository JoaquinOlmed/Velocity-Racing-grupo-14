from Funciones import *

def main():

    lst_nombres=[]
    lst_numero=[]
    lst_escuderia=[]
    lst_puntos=[]
    lst_vueltaProm=[]
    lst_presupuesto=[]
    lst_dnf=[]
    
    opcionesMenu()
    opciones = ingresar_opcionesMenu(1, 8)

    while opciones != 8:
        if opciones == 1:
            print("Registro de piloto")
            altadePilotos(lst_nombres ,lst_numero, lst_escuderia, lst_puntos ,lst_vueltaProm ,lst_presupuesto, lst_dnf)

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