from rec_datos import elegir_Evento, opcion_simp, ingresar_cadena, porque, ingreso_hora, ingreso_fecha,lugar
import base_Evento
import time

def cargar_Evento():
    '''
    -Dia= True (bueno), False (malo) -sentidos 
    -evento STRING (DICCIONARIO)     -presencial_virtual_mixto
    -lugar STRING (INGRESAR)         -dia TUPLA   -hora TUPLA
    -cant.personas.conocidas INT  -cant.personas.desconocidas INT 
    -apoyo-amigos true o false    -querias_ir true o false           - dormi true o false
    -llegada, a tiempo-tarde-temprano       -horas que estuve: INT
    
    -Observacion del evento STTRING
    -Cuantas horas tenia que quedarme para la proxima. INT          -observacion para futuro - STRING
    '''
    eventos = base_Evento.cargar()
    nuevo_id = max([e.get('id', 0) for e in eventos], default=0) + 1
    
    evento = elegir_Evento ()
    
    dia_BM = opcion_simp ("¿Fue un día bueno? s/n: ") #tipo de dia: bueno o malo
    dia_BM = ingresar_cadena (dia_BM,'Día bueno', 'Dia malo')
    
    time.sleep(2)
    
    dormir = opcion_simp ("¿Dormiste seguido? s/n: ")
    dormir = ingresar_cadena (dormir,'mas de 6hs','cero o menos de 6hs') 
    time.sleep(1)
    dia_det = porque (dia_BM) #detalles del día
    
    time.sleep(2)
    
    modalidad = opcion_simp ('¿Fue presencial? s/n:') #tipo de modalidad, virtual o presencial
    modalidad = ingresar_cadena(modalidad,'Presencial','Virtual')
    
    time.sleep(3)
        
    lugar_evento= lugar() # Nombre y direccion(prov, localidad,obs) 
    fecha = ingreso_fecha() # dd-mm-aaaa
    hora = ingreso_hora() # hh:mm
    
    cant_pers_conoc = int(input("cant. personas conocidas: "))
    cant_pers_desco = int(input("cant. personas desconocidas: "))
    
    Amix_apoyo1 = opcion_simp ("¿Alguien de referencia/amix de apoyo estuvo contigo? (tatto, jacque, martin) s/n: ")
    Amix_apoyo = ingresar_cadena (Amix_apoyo1,'Estuve con tatto, jacque o martin', 'Lo hice sola')
    
    queria_preg = opcion_simp ("¿querias ir? s/n: ")
    queria_preg  = ingresar_cadena (queria_preg,'Si, queria ir al lugar','No queria pero debía')
    
    llegada = opcion_simp ("¿Llegaste a tiempo? s/n: ")
    if (llegada):
        llegada_tiempo = 'Llegar a tiempo'
    else:
        llegada_tiempo = opcion_simp ("¿Llegaste temprano? s/n: ")
        if(llegada_tiempo):
            llegada_tiempo ='Llegue temprano - mas de 30 minutos-'
        else:
            llegada_tiempo ='Llegue tarde -más de 15 min-'
    
    print('Cuantas Horas estuviste en el lugar. ')    
    horas_estuve = ingreso_hora()
    
    observacion_evento = input('Observacion del evento: ')
    
    print('¿Cuántas horas debieron ser para no estar mal?: ')
    horas_bien = ingreso_hora()
    obseracion_futura = input('Observaciones para el futuro: ')
    
    evento = {
        'id' : nuevo_id,
        'Dia_BM' : dia_BM,
        'Dormir' : dormir,
        'Detalle del dia' : dia_det,
        'Modalidad' : modalidad,
        'Lugar' : lugar_evento,
        'Fecha': fecha,
        'Hora' : hora,
        'Cant. Pers. Conoc.' : cant_pers_conoc,
        'Cant. Pers. Conoc.' : cant_pers_desco,
        'Amix_apoyo' : Amix_apoyo,
        'queria_preg' : queria_preg,
        'llegada_tiempo' : llegada_tiempo,
        'horas_estuve' : horas_estuve,
        'observacion_evento' : observacion_evento,
        'horas_bien' : horas_bien,
        'obseracion_futura' : obseracion_futura}
    
    eventos = base_Evento.cargar()
    eventos.append(evento)
    base_Evento.guardar (eventos)
    print('Evento guardado.')
    
    return evento
