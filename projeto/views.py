from django.shortcuts import render

def projeto(request):
    return render(request, 'projeto/projeto.html')
