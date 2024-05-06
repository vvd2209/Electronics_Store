from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from electronics_store.models import Supplier, Contact, Product


class SupplierTestCase(APITestCase):
    """ Класс тестирования модели поставщика. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='test@test.ru',
            password='test'
        )

        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(
            company_name='Test',
            link_type='Factory',
            owner=self.user
        )

    def test_create_supplier(self):
        """ Тестирование создания нового поставщика. """

        data = {
            'company_name': 'Test',
            'link_type': 'Factory'
        }

        response = self.client.post(
            '/supplier/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_supplier_list(self):
        """ Тестирование просмотра списка поставщиков. """

        response = self.client.get(
            '/supplier/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json()['count'], 1)

    def test_view_supplier_detail(self):
        """ Тестирование просмотра деталей поставщика. """

        response = self.client.get(
            f'/supplier/{self.supplier.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_contact_in_supplier(self):
        """ Тестирование обновления полей контактных данных у поставщика. """

        data = {
            'house_number': '1'
        }

        response = self.client.patch(
            f'/supplier/{self.supplier.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_dont_update_debt(self):
        """ Тестирование поля задолженности. """

        data = {
            'debt': 100.00
        }

        response = self.client.patch(
            f'/supplier/{self.supplier.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json()['debt'], '0.00')

    def test_delete_supplier(self):
        """ Тестирование удаления поставщика. """

        response = self.client.delete(
            f'/supplier/{self.supplier.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str_method(self):
        """ Тестирование метода str модели поставщика. """

        str_data = f"{self.supplier.company_name}"

        self.assertEqual(str(self.supplier), str_data)


class ContactTestCase(APITestCase):
    """ Класс тестирования модели контактных данных. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='test@test.ru',
            password='test'
        )

        self.client.force_authenticate(user=self.user)

        self.contact = Contact.objects.create(
            city='Test',
            country='Test',
            creator=self.user
        )

    def test_create_contact(self):
        """ Тестирование создания новых контактных данных. """

        data = {
            'city': 'Test',
            'country': 'Test'
        }

        response = self.client.post(
            '/contact/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_contact_list(self):
        """ Тестирование просмотра списка контактных данных. """

        response = self.client.get(
            '/contact/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_view_contact_detail(self):
        """ Тестирование просмотра деталей контактных данных. """

        response = self.client.get(
            f'/contact/{self.contact.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_contact(self):
        """ Тестирование редактирования контактных данных. """

        data = {
            'email': 'test1@test.com'
        }

        response = self.client.patch(
            f'/contact/{self.contact.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_contact(self):
        """ Тестирование удаления контактных данных. """

        response = self.client.delete(
            f'/contact/{self.contact.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str_method(self):
        """ Тест метода str модели контактных данных. """

        str_data = f"{self.contact.city}, {self.contact.country}"

        self.assertEqual(str(self.contact), str_data)


class ProductTestCase(APITestCase):
    """ Класс тестирования модели товаров. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='test@test.ru',
            password='test'
        )

        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(
            company_name='Test',
            link_type='Factory',
            owner=self.user
        )

        self.product = Product.objects.create(
            title='Test',
            model='Test',
            supplier=self.supplier
        )

    def test_create_product(self):
        """ Тестирование создания новых товаров. """

        data = {
            'title': 'Test',
            'model': 'Test'
        }

        response = self.client.post(
            '/product/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_product_list(self):
        """ Тестирование просмотра списка товаров. """

        response = self.client.get(
            '/product/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json()[0]['supplier'], self.supplier.id)

    def test_view_product_detail(self):
        """ Тестирование просмотра деталей товара. """

        response = self.client.get(
            f'/product/{self.product.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_product(self):
        """ Тестирование редактирования товара. """

        data = {
            'title': 'Test1'
        }

        response = self.client.patch(
            f'/product/{self.product.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_product(self):
        """ Тестирование удаления товара. """

        response = self.client.delete(
            f'/product/{self.product.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str_method(self):
        """ Тестирование метода str модели товара. """

        str_data = f"{self.product.title} ({self.product.model})"

        self.assertEqual(str(self.product), str_data)
