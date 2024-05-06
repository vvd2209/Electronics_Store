from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Права доступа для владельца. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request, view, obj):
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.owner


class IsProductOwner(BasePermission):
    """ Права доступа для владельца. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request, view, obj):
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.supplier.owner


class IsContactCreator(BasePermission):
    """ Права доступа для владельца. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request, view, obj):
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.creator


class IsSuperUser(BasePermission):
    """ Права доступа для супер пользователя. """
    message = 'Вы не являетесь супер пользователем.'

    def has_permission(self, request, view):
        """ Настраивает способ проверки разрешений. """
        return request.user.is_superuser
