from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from .serializers import ClientsSerializer
from ..models import Clients


class ClientsViewSet(ListModelMixin, GenericViewSet):

    serializer_class = ClientsSerializer
    queryset = Clients.objects.all()
    authentication_classes = [TokenAuthentication, ]
