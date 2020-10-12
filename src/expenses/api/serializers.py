from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Expenses, Types


class ExpensesTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = '__all__'


class ExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses
        fields = '__all__'
