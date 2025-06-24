import json
import menu
import time

def cargar():
    try:
        with open('eventos.json','r') as archivo:
            eventos = json.load(archivo)
    except FileNotFoundError:
        eventos = []
    return eventos

def guardar(eventos):
    with open('eventos.json', 'w') as archivo:
        json.dump(eventos, archivo, indent=4)

def ver_Lista():
    '''    eventos = cargar()
    if eventos:
        for id in eventos:
            print(id)
        #busca
    else:
        print("No hay datos de estudiantes almacenados.")
        time.sleep(3)
        menu.menu_Inicial()
    return
'''

    eventos = cargar()
    
    if not eventos:
        print("No hay eventos cargados.")
        return

    print("\nListado completo de eventos:")
    print("=" * 50)

    for i, evento in enumerate(eventos, 1):
        print(f"\nEvento #{i}")
        print("-" * 50)
        for clave, valor in evento.items():
            # Alinea la clave a la izquierda con 30 caracteres
            print(f"{str(clave).ljust(30)}: {valor}")
    print("=" * 50)