from rest_framework import serializers

from electronics_store.models import Supplier, Product, Contact


class ContactSerializer(serializers.ModelSerializer):
    """ Сериализатор для контактных данных. """

    class Meta:
        """ Метаданные сериализатора. """
        model = Contact
        fields = ('email', 'country', 'city', 'street', 'house_number',)


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для товаров. """

    class Meta:
        """ Метаданные сериализатора. """
        model = Product
        fields = ('title', 'model', 'launch_date', 'supplier',)


class SupplierSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели поставщика. """

    contact = ContactSerializer(source='contacts')
    product_list = ProductSerializer(
        source='product_set',
        many=True,
        read_only=True
    )

    def update(self, instance, validated_data):
        """ Обновление контактной информации через поставщика. """
        contact_data = validated_data.pop('contacts', None)

        if contact_data:
            contact_serializer = ContactSerializer(
                instance=instance.contacts,
                data=contact_data
            )

            if contact_serializer.is_valid():
                contact_serializer.save()

        return instance

    class Meta:
        """ Метаданные сериализатора. """
        model = Supplier
        fields = (
            'company_name', 'link_type', 'supplier_name',
            'debt', 'created_at', 'product_list', 'contact',
        )
        read_only_fields = ('debt', 'created_at',)


class SupplierCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания поставщика. """

    class Meta:
        """ Метаданные сериализатора. """
        model = Supplier
        fields = ('company_name', 'link_type', 'supplier_name', 'debt',)
