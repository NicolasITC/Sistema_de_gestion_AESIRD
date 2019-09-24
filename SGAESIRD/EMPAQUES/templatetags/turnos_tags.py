from django import template
from ..models import Turnos
import datetime
from datetime import timedelta
import dateutil.parser

register = template.Library()

@register.simple_tag
def comparar(dia, hora, turnos):
    resultado = turnos.filter(fecha=dia, hora_inicio=hora.strftime("%H:%M:%S"))
    print("#########################################")
    print(resultado)
    return resultado

