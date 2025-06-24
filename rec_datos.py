import fecha
import time

def elegir_Evento ():
    cont= 0
    tipos_eventos = ('otro','Casa', 'Cumpleanios', 'Jodas','Salidas a comer','Estudios','Visitas anuales')
    for indice in tipos_eventos:
        print (cont ,indice)
        cont += 1
        time.sleep(3)
    print ('|°-----------_-------------°|')
          
    opcion = int(input('Elija un evento: '))
    time.sleep(2)
    if (opcion != 0):
        tipo_evento = tipos_eventos[opcion]
        eventos = {
                'Casa' : {
                    1 : 'Pasada diurna',
                    2 : 'Medio dia - min 3hs',
                    3 : 'Todo el día 8/12hs',
                    4 : 'Dia y noche',
                    5 : 'Solo dormi'},
                'Cumpleanios' : {
                    1 : 'Familia',
                    2 : 'seguro',
                    3 : 'amigxs',
                    4 : 'conocidos_amix',
                    5 : 'conocidos',
                    6 : 'desconocido'},
                'Jodas' : {
                    1 : 'Familia',
                    2 : 'seguro',
                    3 : 'amigxs',
                    4 : 'conocidos_amix',
                    5 : 'conocidos',
                    6 : 'desconocido'},
                'Salidas a comer' : {
                    1 : 'Día (12 a 15)',
                    2 : 'Tarde (15 a 19)',
                    3 : 'Noche (19 a 23)',
                    4 : 'Trasnoche_Madrugada (00 a 7)',
                    5 : 'Mañana (8 y 12)'},
                'Estudios' : {
                    1 : 'Cine',
                    2 : 'Ingenieria',
                    3 : 'Profesorado',
                    4 : 'Curso',
                    5 : 'Practicas'},
                'Visitas anuales' : {
                    1 : 'Familia Bernal',
                    2 : 'Familia Villagra',
                    3 : 'Martin',
                    4 : 'Tatto',
                    5 : 'amixs',
                    6 : 'grupos facu'}}
        time.sleep(2)
        print ('|°-----------_-------------°|')
        for clave, valor in eventos[tipo_evento].items():
            print (clave, valor)

        opcion2 = int(input('Elija una descripcion del evento: '))
        evento = list(eventos[tipo_evento].values())[opcion2]
    else: 
        evento = input('que tipo de evento era?: ')    
    comentario = input('comentario: ')
    Resumen_evento = (tipo_evento,evento,comentario)

    return Resumen_evento

def opcion_simp (cadena):
    opcion = input(cadena)
    while opcion != True and opcion != False and opcion != None:
        if (opcion == "s" or opcion == "S"):
                opcion = True
        elif (opcion == 'n' or opcion == "N"):
                opcion = False
        else:
            print('Elija una opcion valida')
            opcion = input(cadena)
    return opcion

def ingresar_cadena (opcion,cadenaT,cadenaF):
    
    if (opcion):
        cadena=cadenaT
    else:
        cadena=cadenaF
    return cadena
    
def porque (opcion):   
    if (opcion == False):
        porque = input('ingrese como te sentias: ')
    else:
        porque = "En estos días no hubo dolor de cabeza, golpes, dolor de estomago, tristeza constante. Comi, Dormi, fui productiva. En cuanto a los sentidos no fueron una molestia, pude realizar mis actividades sin dolor"
    return porque

def lugar ():
    print ('----- CON RESPECTO AL LUGAR -----')
    nombre = input('¿Cómo se llama?: ')
    prov = input('Provincia: ')
    localidad = input('Localidad: ')
    tipo = input ('Tipo de lugar -edificio, casa... -: ')
    observacion = input ('Detalles sensoriales: ')
    direccion = (prov, localidad, tipo)
    lugar_evento=(nombre,direccion, observacion)
    return lugar_evento

def ingreso_fecha ():
    valido = False
    while valido == False:
        dia = int(input('Día: '))
        mes = int(input('Mes: '))
        anio = int(input('Año: '))
        valido = fecha.fecha_validar(dia, mes, anio)
    fechaevento =  f"{dia:02d}-{mes:02d}-{anio}" #str(dia)+'-'+ str(mes)+'-'+ str(anio)
    return fechaevento

def ingreso_hora ():
    valido = False
    while valido == False:
        hs = int(input('Hora (00-23): '))
        minut = int(input('Minutos (00-59): '))
        if(0 <= hs <= 23 and 0<= minut <= 59):
            valido = True
    fechaevento =  str(hs)+':'+ str(minut)
    return fechaevento