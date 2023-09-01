from django.urls import path

from .views import *

urlpatterns = [
    path('', FlowerHome.as_view(), name='home'),
    path('category/<str:slug>', get_category, name='category')
]