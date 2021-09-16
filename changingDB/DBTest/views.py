from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_temp(request):
    return render(request,template_name='temp_all.html')




def welcome(request):
    return HttpResponse('<h1>Welcome</h1>')