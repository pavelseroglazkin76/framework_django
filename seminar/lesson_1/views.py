from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from lesson_1.models import Brand, Category, Product
from cart.forms import *
from django.views.generic.edit import FormView

logger = logging.getLogger(__name__)

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Условия работы", 'url_name': 'working_conditions'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]


# def index(request):
#     logger.info('Index page accessed')
#     brands = Brand.objects.all()
#     products = Product.objects.order_by("-id")[0:8]
#     context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'brands': brands,
#         'products': products
#     }
#     return render(request, 'lesson_1/index.html', context=context)


class FlowerHome(ListView, FormView):
    model = Product
    template_name = 'lesson_1/index.html'
    context_object_name = 'products'
    form_class = CartAddProductForm
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.all()
        context['title'] = 'Главная страница'
        context['brands'] = brands
        context['menu'] = menu
        return context

    # def get_queryset(self):
    #     return Product.objects.order_by("-id")[0:8]


class ProductCategory(ListView, FormView):
    model = Product
    template_name = 'lesson_1/category.html'
    context_object_name = 'products'
    form_class = CartAddProductForm
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], status=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['products'][0].category)
        return context


def about(request):
    logger.info('About page accessed')
    return render(request, 'lesson_1/about.html', {'menu': menu, 'title': 'О нас'})


def news(request):
    logger.info('News page accessed')
    return HttpResponse('Новости')


def working_conditions(request):
    logger.info('Working_conditions page accessed')
    return HttpResponse('Условия работы')


def reviews(request):
    logger.info('Reviews page accessed')
    return HttpResponse('Отзывы')


def contacts(request):
    logger.info('Contacts page accessed')
    return HttpResponse('Контакты')


def articles(request):
    logger.info('Articles page accessed')
    return HttpResponse('Статьи')


class ShowProduct(DetailView, FormView):
    model = Product
    template_name = 'lesson_1/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    form_class = CartAddProductForm


# def form(request):
#     context = {}
#     context['form'] = GeeksForm()
#
#     return render(request, "lesson_1/form.html", context=context)


class Search(ListView):
    template_name = 'lesson_1/search.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context