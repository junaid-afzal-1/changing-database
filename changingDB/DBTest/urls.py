from . import views
from django.urls import path
urlpatterns = [
    path('temp-all/',views.all_temp),
    path('welcome/',views.welcome),
]
