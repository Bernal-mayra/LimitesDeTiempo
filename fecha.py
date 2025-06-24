def es_bisiesto(anio):
    if (anio%4==0 and anio%400==0):
        salida=True
        
    elif (anio%4==0 and anio%100!=0 and anio%400!=0):
        salida=True        
    else:
        salida=False
    return salida

def cant_dias_mes (mes, anio):

    if (mes==1 or mes==3 or mes==5)or(mes==7 or mes==8 or mes==10 or mes==12):
        #print("30 dias")
        dia = 31
    elif (mes==4 or mes==6 or mes==9 or mes==11):
        #print("31 dias")
        dia = 30
    elif (mes == 2):
        if (es_bisiesto (anio)):
            #print('29 dias')
            dia=29
        else:
            #print('28 dias')
            dia=28
    return dia

def fecha_validar(dia,mes,anio):
    fecha = False
    if (anio>=1994 and anio<=2030 ):   
        if (mes<=12 and mes>0):
            cant_dia = cant_dias_mes(mes,anio)
            if (dia<=cant_dia and dia>0 ):
                fecha=True
    return fecha