from django import template
from datetime import date,datetime
register = template.Library()

@register.filter
def jijig(value):
    return value.lower()
@register.filter
def tom(value):
    return value.upper()
    
@register.filter
def unuudur(value):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    return d1

@register.filter
def dt(value):
    d2=value
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    asd = datetime.strptime(d1, "%Y-%m-%d")
    asd2 = datetime.strptime(d2, "%Y-%m-%d")
    delta = asd - asd2
    if delta.days == 0:
        return "Өнөөдөр"
    elif delta.days > 0:
        if delta.days>30 and delta.days<365 :
            z=int(delta.days/30)
            x=delta.days%30
            return f"{z} сар {x} өдрийн өмнө"
        elif delta.days>365:
            y=int(delta.days/365)
            z=int((delta.days-(y*365))/30)
            x=delta.days%30
            if z==0:
                return f"{y} жил {x} өдрийн өмнө"
            else:
                return f"{y} жил {z} сар {x} өдрийн өмнө"
        else:
            return f"{delta.days} өдрийн өмнө"

    elif delta.days < 0:
        dra = abs(delta.days)
        if dra>30 and dra<365 :
            z=int(dra/30)
            x=dra%30
            return f"{z} сар {x} өдрийн дараа"
        elif dra>365:
            y=int(dra/365)
            z=int((dra-(y*365))/30)
            x=dra%30
            if z==0:
                return f"{y} жил {x} өдрийн дараа"
            else:
                return f"{y} жил {z} сар {x} өдрийн дараа"
        else:
            return f"{dra} өдрийн дараа"
        


    