from django.shortcuts import render
from django.shortcuts import HttpResponse



def home (request): 
    return render(request, 'home.html')
def sobre (request): 
    return HttpResponse('sobre')
def contato (request):
    return HttpResponse('contato')
