from django.db import models
from django.conf import settings
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """ Модель контактных данных. """
    email = models.EmailField(verbose_name='E-mail', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='Страна')
    city = models.CharField(max_length=25, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома',
        **NULLABLE
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Создатель',
        **NULLABLE
    )

    def __str__(self):
        """ Строковое представление модели контактов. """
        return f"{self.city}, {self.country}"

    class Meta:
        """ Метаданные модели контактов. """
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные данные'


class Supplier(models.Model):
    """ Модель поставщика. """

    LINK_TYPE_CHOICES = (
        ('Factory', 'Завод'),
        ('Retail Network', 'Розничная сеть'),
        ('Individual Entrepreneur', 'ИП'),
    )

    company_name = models.CharField(
        max_length=100,
        verbose_name='Название компании',
    )
    link_type = models.CharField(
        choices=LINK_TYPE_CHOICES,
        verbose_name='Тип звена'
    )
    contacts = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        verbose_name='Контактная информация',
        **NULLABLE
    )
    supplier_name = models.ForeignKey(
        'Supplier',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        **NULLABLE
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Задолженность'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время создания'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        **NULLABLE
    )

    def __str__(self):
        """ Возвращает строковое представление о модели поставщика. """
        return f"{self.company_name}"

    class Meta:
        """ Метаданные модели поставщика. """
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """ Модель товара. """
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель товара')
    launch_date = models.DateField(verbose_name='Дата выхода', **NULLABLE)
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE,
        verbose_name='Поставщик',
        **NULLABLE
    )

    def __str__(self):
        """ Возвращает строковое представление о модели товара. """
        return f"{self.title} ({self.model})"

    class Meta:
        """ Метаданные модели товара. """
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
