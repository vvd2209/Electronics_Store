from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsSuperUser, IsOwner
from users.serializers import UserSerializer, UserProfileSerializer, UserCreateSerializer


class UserViewSet(ModelViewSet):
    """ Сет представлений для модели пользователя """
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'create': UserCreateSerializer,
        'retrieve': UserProfileSerializer,
        'update': UserProfileSerializer,
    }

    def get_object(self):
        """ Получает текущего пользователя """
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        """ Action destroy устанавливает is_active в False """
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        """ Возвращает сериализатор в зависимости от выбора запроса """
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """ Возвращает права в зависимости от статуса пользователя """
        match self.action:
            case 'create':
                permission_classes = [AllowAny]
            case 'list':
                permission_classes = [IsAuthenticated, IsSuperUser]
            case _:
                permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]

        return [permission() for permission in permission_classes]
