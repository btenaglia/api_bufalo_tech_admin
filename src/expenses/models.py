from __future__ import unicode_literals

from django.db import models

from utils.models import BaseCreatedUpdatedModel


class Types(BaseCreatedUpdatedModel):

    name = models.CharField('Tipo del gasto', max_length=150)


class Expenses(BaseCreatedUpdatedModel):

    type = models.ForeignKey('expenses.Types', on_delete=models.PROTECT)
    amount = models.DecimalField('Price', max_digits=8, decimal_places=2)
    date = models.DateField('Fecha', null=True, blank=True)
