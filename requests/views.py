from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME 2')

def pedidos(request):
    return HttpResponse('PEDIDOS 2')

def status_pedidos(request):
    return HttpResponse('STATUS PEDIDOS 2')