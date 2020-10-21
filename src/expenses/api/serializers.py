from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Expenses, Types


class ExpensesTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = ['id', 'name', ]


class ExpensesSerializer(serializers.ModelSerializer):

    type = ExpensesTypesSerializer(read_only=True)

    class Meta:
        model = Expenses
        fields = ['id', 'type', 'date']
