from .models import Temp


def temp_emp(request):
    return {'temp_emp':[Temp.objects.all()]}