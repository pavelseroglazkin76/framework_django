from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='Имя категории')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Brand(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название фирменного знака')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    MAYBECHOICE = [
        (0, 'No'),
        (1, 'Yes'),
    ]
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Фирменный знак', on_delete=models.CASCADE)
    title = models.CharField(max_length=225, verbose_name='Наименование')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
    #image = models.ImageField(verbose_name='Изображение')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Старая цена')
    status = models.PositiveSmallIntegerField(choices=MAYBECHOICE, blank=False, default=1, verbose_name='Статус')
    depart = models.CharField(max_length=225, verbose_name='Упаковка', blank=True)
    article = models.CharField(max_length=225, verbose_name='Артикуль', blank=True)
    grade = models.CharField(max_length=225, verbose_name='Класс', blank=True)
    hieght = models.CharField(max_length=100, verbose_name='Высота', blank=True)
    flower_size = models.CharField(max_length=225, verbose_name='Размер цветка', blank=True)
    flowering_period = models.CharField(max_length=100, verbose_name='Период', blank=True)
    landing_place = models.CharField(max_length=100, verbose_name='Место посадки', blank=True)
    frost_resistance = models.CharField(max_length=100, verbose_name='Морозостойкость', blank=True)

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return 'Продукт: {} для корзины'.format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=225, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.first_name, self.user.last_name)
