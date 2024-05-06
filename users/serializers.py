from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели пользователя """

    class Meta:
        """ Метаданные сериализатора """
        model = User
        fields = ('email', 'first_name', 'is_active',)


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания пользователя """

    class Meta:
        """ Метаданные сериализатора """
        model = User
        fields = ('email', 'first_name', 'last_name', 'password',)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Сериализатор для профиля пользователя """

    class Meta:
        """ Метаданные сериализатора """
        model = User
        fields = ('email', 'first_name', 'last_name')
