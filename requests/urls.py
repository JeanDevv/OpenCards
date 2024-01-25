from django.urls import path
from requests.views import home, pedidos, status_pedidos


#   dominio.com/requests/home
urlpatterns = [
    path('', home), # Home
    path('pedidos/', pedidos), #Pedidos
    path('status_pedidos/', status_pedidos) #Status do Pedidos
]