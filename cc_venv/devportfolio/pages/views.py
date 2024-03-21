from django.shortcuts import render

from base.models import Developer



def home(request):

    

    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/service.html')


def contact(request):
    return render(request, 'pages/contact.html')

def devcolaborators(request):
    developeur = Developer.objects.all()
    data = {

        'devs': developeur
    }
    return render(request, 'pages/devcolabs.html', data)

