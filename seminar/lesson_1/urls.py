from django.urls import path

from .views import *

urlpatterns = [
    path('', FlowerHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('working_conditions/', working_conditions, name='working_conditions'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', contacts, name='contacts'),
    path('articles/', articles, name='articles'),
    path('category/<str:cat_slug>', ProductCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
    # path('form/', form, name='form'),
    path('search/', Search.as_view(), name='search'),
]