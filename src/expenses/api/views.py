from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from .serializers import ExpensesSerializer, ExpensesTypesSerializer
from ..models import Expenses, Types


class TypesViewSet(ListModelMixin, GenericViewSet):
    """ Expenses types """

    serializer_class = ExpensesTypesSerializer
    queryset = Types.objects.all()
    authentication_classes = [TokenAuthentication, ]


class ExpensesViewSet(ListModelMixin, GenericViewSet, CreateModelMixin):
    """ Expenses """

    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    authentication_classes = [TokenAuthentication, ]

    def create(self, request, *args, **kwargs):
        pass
