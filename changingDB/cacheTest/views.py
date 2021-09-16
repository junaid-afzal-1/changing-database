from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.cache import cache 
from django.core.cache.backends.base import DEFAULT_TIMEOUT


def cache_test(request):
    
    #radis_cache = radis_cache['default']

    ip = str(request.META.get('REMOTE_ADDR'))

    cache.set(ip,'2',timeout=22)
    print(ip)
    print(cache.get(ip))

    #print(radis_cache.get(1))


    return HttpResponse(str(cache.keys('*')))






