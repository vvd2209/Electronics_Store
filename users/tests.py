from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Класс тестирования модели пользователя. """
    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """
        self.user = User.objects.create(
            email='test@test.ru',
            password='test'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ Тестирование регистрации нового пользователя. """
        data = {
            'email': 'test1@test.ru',
            'password': 'test'
        }
        response = self.client.post(
            '/users/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_superuser(self):
        """ Тестирование создания суперпользователя. """
        self.momo = User.objects.create_superuser(
            email='test2@test.ru',
            password='test'
        )
        self.assertEqual(self.momo.is_superuser, True)

    def test_create_superuser_errors(self):
        """ Тестирование создания суперпользователя со статусами is_staff, is_superuser - False. """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='test@test.ru',
                password='test',
                is_staff=False
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='test@test.ru',
                password='test',
                is_superuser=False
            )

    def test_create_superuser_without_email(self):
        """ Тестирование создания суперпользователя со статусами is_staff, is_superuser - False. """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(password='test', email=None)

    def test_view_user_list(self):
        """ Тестирование просмотра списка пользователей. """
        # Просматривать список может только суперпользователь.
        response = self.client.get(
            '/users/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(
            response.json(),
            {
                'detail': 'Вы не являетесь супер пользователем.'
            }
        )

    def test_view_user_detail(self):
        """ Тестирование просмотра профиля пользователя. """
        response = self.client.get(
            f'/users/{self.user.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_user(self):
        """ Тестирование редактирования профиля пользователя. """
        data = {
            'email': 'test@test.ru',
        }
        response = self.client.put(
            f'/users/{self.user.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self):
        """ Тестирование удаления профиля пользователя. """
        response = self.client.delete(
            f'/users/{self.user.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str_method_email(self):
        """ Тестирование метода str модели пользователя. """
        str_data = f"{self.user.email}"
        self.assertEqual(str(self.user), str_data)

    def test_str_method_name(self):
        """ Тестирование метода str модели пользователя. """
        self.user.first_name = 'test@test.ru'
        str_data = f"{self.user.first_name}"
        self.assertEqual(str(self.user), str_data)
