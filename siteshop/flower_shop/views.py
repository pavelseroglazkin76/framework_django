from django.shortcuts import render


def index(request):
    return render(request, 'flower_shop/index.html')


def get_category(request):
    return render(request, 'flower_shop/category.html')
