from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import ProvidersSerializer
from ..models import Providers


class ProvidersViewSet(ListModelMixin, GenericViewSet):

    serializer_class = ProvidersSerializer
    queryset = Providers.objects.all()

