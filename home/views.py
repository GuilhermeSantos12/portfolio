from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def projeto(request):
    return render(request, 'projeto/projeto.html')