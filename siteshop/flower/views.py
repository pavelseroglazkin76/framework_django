from django.shortcuts import render


def index(request):
    return render(request, 'flower/index.html')


def get_category(request):
    return render(request, 'flower/category.html')
