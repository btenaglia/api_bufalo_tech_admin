from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import ExpensesSerializer, ExpensesTypesSerializer
from ..models import Expenses, Types


class TypesViewSet(ListModelMixin, GenericViewSet):
    """ Expenses types """

    serializer_class = ExpensesTypesSerializer
    queryset = Types.objects.all()


class ExpensesViewSet(ListModelMixin, GenericViewSet):

    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()

