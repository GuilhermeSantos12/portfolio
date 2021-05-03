from django.shortcuts import render
from django.http import HttpResponse
import mimetypes


def index(request):
    return render(request, 'home/index.html')

def projeto(request):
    return render(request, 'projeto/projeto.html')



