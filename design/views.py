from django.shortcuts import render


def index(request):
    return render(request, 'design/about.html')


def cv(request):
    return render(request, 'design/CV.html')