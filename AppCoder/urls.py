from django.urls import path, include
from AppCoder.views import curso, entregable, inicio
urlpatterns = [
    path('/', inicio),
    path('curso/', curso,),
    path('entregable', entregable),
    ]