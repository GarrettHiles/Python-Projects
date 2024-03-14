
from django.shortcuts import render

def home(request):
    persons = [ "Jake", "Payton", "Carson", "Alex", "Aiden", "Ryan"]
    context = {'persons': persons
    }
    return render(request, 'home.html', context)
