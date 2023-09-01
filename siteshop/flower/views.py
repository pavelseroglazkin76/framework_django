from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# def index(request):
#     return render(request, 'flower/index.html')
class FlowerHome(ListView):
    model = Product
    template_name = 'flower/index.html'
    #context_object_name = 'product'
    #extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.all()
        context['title'] = 'Главная страница'
        context['brands'] = brands
        return context

    def get_queryset(self):
        return Product.objects.order_by("-id")[0:8]


def get_category(request):
    return render(request, 'flower/category.html')
