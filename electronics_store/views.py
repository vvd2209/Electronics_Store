from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics_store.models import Supplier, Contact, Product
from electronics_store.paginators import SupplierPaginator
from electronics_store.permissions import (IsOwner, IsSuperUser, IsProductOwner, IsContactCreator)
from electronics_store.serializers import (SupplierSerializer, ContactSerializer, ProductSerializer, SupplierCreateSerializer)


class SupplierViewSet(ModelViewSet):
    """ Сет представлений для модели поставщика. """
    queryset = Supplier.objects.all()
    # Сериализаторы для представлений.
    default_serializer = SupplierSerializer
    pagination_class = SupplierPaginator
    serializers = {
        'create': SupplierCreateSerializer,
    }

    def get_queryset(self):
        """ Осуществляет фильтрацию объектов по определенной стране. """
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)
        return queryset

    def perform_create(self, serializer):
        """ Сохраняет текущего пользователя как владельца при создании. """
        new_link = serializer.save()
        new_link.owner = self.request.user
        new_link.save()

    def get_serializer_class(self):
        """ Возвращает сериализатор в зависимости от выбора запроса. """
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """ Возвращает права в зависимости от статуса пользователя. """
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]

        return [permission() for permission in permission_classes]


class ProductViewSet(ModelViewSet):
    """ Сет представлений для модели товара. """
    queryset = Product.objects.all()
    # Сериализаторы для представлений.
    serializer_class = ProductSerializer

    def get_permissions(self):
        """ Возвращает права в зависимости от статуса пользователя. """
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [
                    IsAuthenticated, IsProductOwner | IsSuperUser
                ]

        return [permission() for permission in permission_classes]


class ContactViewSet(ModelViewSet):
    """ Сет представлений для модели товара. """
    queryset = Contact.objects.all()
    # Сериализаторы для представлений.
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        """ Сохраняет текущего пользователя как создателя при создании. """
        new_contact = serializer.save()
        new_contact.creator = self.request.user
        new_contact.save()

    def get_permissions(self):
        """ Возвращает права в зависимости от статуса пользователя. """
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [
                    IsAuthenticated, IsContactCreator | IsSuperUser
                ]

        return [permission() for permission in permission_classes]
