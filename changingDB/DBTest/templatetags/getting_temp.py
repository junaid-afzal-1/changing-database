from DBTest.models import Temp
from django import template

register = template.Library()


@register.simple_tag(name='obj')
def return_all_temps():
    #obj = "hello"
    #obj = Temp.objects.all()
    obj = [1,2,3,4]
    return obj



@register.simple_tag
def return_t(t):

    obj = Temp.objects.all()

    for i in obj:
        if i.name == t:
            return i.time

    

    return 'No Record Found'

