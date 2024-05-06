from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    """ Модель представления класса Пользователь, наследуемая от абстрактного класса """
    username = None  # исключение поля "username", так как вместо него будет использовано поле "email"

    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = "email"  # указание на то, что поле "email" будет использоваться для идентификации пользователя
    REQUIRED_FIELDS = []  # поля, которые будут запрашиваться при создании пользователя через команду createsuperuser

    objects = UserManager()

    def __str__(self):
        """ Метод представления модели в виде строки """
        return f"{self.email}"

    class Meta:
        """ Метаданные модели """
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
