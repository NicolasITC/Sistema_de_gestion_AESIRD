from django import template
from ..models import Turnos
import datetime
from datetime import timedelta
import dateutil.parser

register = template.Library()

@register.simple_tag
def get_turnos(actual, turno):
    if(actual>=0):
        hoy=datetime.datetime.today()+ datetime.timedelta(weeks=actual)
    else:
        hoy=datetime.datetime.today()- datetime.timedelta(weeks=abs(actual))
    week=hoy.strftime("%Y-W%W") 
    start_week = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")

    end_week = start_week + datetime.timedelta(days=6)

    semana = turno.filter(fecha__range=[start_week,end_week])
    return semana

@register.simple_tag
def get_semana(actual):
    if(actual>=0):
        hoy=datetime.datetime.today()+ datetime.timedelta(weeks=actual)
    else:
        hoy=datetime.datetime.today()- datetime.timedelta(weeks=abs(actual))
        
    week=hoy.strftime("%Y-W%W") 
    start_week = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")
    end_week = start_week + datetime.timedelta(days=6)   
    start_week = dateutil.parser.parse(str(start_week)).date()
    date_list = [start_week + datetime.timedelta(days=x) for x in range(7)]
    return date_list

@register.simple_tag
def comparar(dia, hora, turnos):
    resultado = turnos.filter(fecha=dia, hora_inicio=hora.strftime("%H:%M:%S"))
    print("#########################################")
    print(resultado)
    return resultado

