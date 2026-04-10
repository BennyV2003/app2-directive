from django.shortcuts import render

def index(request):
    return render(request, 'directive/index.html')