from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home (request):
    return render (request, 'generator/home.html')

def about (request):
        return render (request, 'generator/about.html')


def password (request):

        Characters = list ('abcdefghijklmnopqrstuvwxyz')

        if request.GET.get('uppercase'):
            Characters.extend(list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.GET.get('special'):
            Characters.extend(list ('!@#$%^&*()_+?><'))

        if request.GET.get('numbers'):
            Characters.extend(list ('1234567890'))

        Length = int(request.GET.get('Length' , 8))

        thepassword = ''
        for x in range (Length):
            thepassword += random.choice (Characters)


        return render (request, 'generator/password.html', {'password': thepassword})
