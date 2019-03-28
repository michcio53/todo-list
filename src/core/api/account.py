from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from core.serializers.account import UserCreateSerializer


class AccountAPIViewSet(GenericViewSet):

    # for login user base auth
    @action(detail=False, methods=['POST'], serializer_class=UserCreateSerializer, url_path='register')
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Ok", status=status.HTTP_201_CREATED)


