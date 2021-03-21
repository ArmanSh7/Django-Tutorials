from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request:HttpRequest)->HttpResponse:
    return render(request, 'index.html')
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))
def contact(request:HttpRequest)->HttpResponse:
    return render(request, 'contact.html')

def about(request:HttpRequest)->HttpResponse:
    return render(request, 'about.html')

