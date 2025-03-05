from django.shortcuts import render
from django.shortcuts import HttpResponse



def home (request): 
    return HttpResponse('Home')
def sobre (request): 
    return HttpResponse('sobre')
def contato (request):
    return HttpResponse('contato')
