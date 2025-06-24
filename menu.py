from funciones_princ import cargar_Evento
from base_Evento import ver_Lista
import time

def menu_Inicial():
    """Las opciones del menu"""
    print('''
    \t :::Menú del sistema de Gestion de tiempo social
    (aunque te guste algo no significa que no produce
    cansancio y malestar.
    ):::
    1 - Buscar Evento
    2 - Ver lista de lugares y Tiempos
    3 - Agregar Eventos
    4 - Modificar datos
    5 - Eliminar estudiantes
    6 - Salir''')
    
    accion_Menu()
    return

def accion_Menu():
    """interaccion del usuario con el menu"""
    opcion_menu = int(input("Ingrese una opción (1-6):  "))
    time.sleep(2)
    print ('|°-----------_-------------°|')      
    if opcion_menu == 1:
        print('1')
        #buscar_Evento
    elif opcion_menu == 2:
        ver_Lista()
        
    elif opcion_menu == 3:
        cargar_Evento()
        
    elif opcion_menu == 4:
        print('4')
        #modificar_Evento()
    elif opcion_menu == 5:
        print ('5')
        #eliminar_Carga() 
    elif opcion_menu == 6:
        print('No te sobre exijas')
    else:
        print('Opción no valida, ingrese las opciones disponibles')
        menu_Inicial()
    return
