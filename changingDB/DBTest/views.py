from django.shortcuts import render

# Create your views here.

def all_temp(request):
    return render(request,template_name='temp_all.html')