from django.shortcuts import render
from random import choice

def home(request):
    return render(request, 'passgenerator/home.html')

def about(request):
    return render(request,'passgenerator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specila'):
        characters.extend(list("!@#$%^&*()-_=+[]{/}|;:',.<> ?"))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    pass_generator = ''
    for x in range(length):
        pass_generator += choice(characters)
    
    return render(request,'passgenerator/pass.html', {'password': pass_generator})
