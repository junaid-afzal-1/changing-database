from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.cache import cache as radis_cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT


def cache_test(request):
    
    #radis_cache = radis_cache['default']

    ip = str(request.META.get('REMOTE_ADDR'))

    radis_cache.set(ip,'2',timeout=0)
    print(ip)
    print(radis_cache.get(ip))

    #print(radis_cache.get(1))


    return HttpResponse(str(radis_cache.get('objects')))






