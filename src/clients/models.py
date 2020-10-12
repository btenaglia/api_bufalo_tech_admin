from __future__ import unicode_literals

from django.db import models

from utils.models import BaseCreatedUpdatedModel


class Clients(BaseCreatedUpdatedModel):

    name = models.CharField('Nombre', max_length=150)
    email = models.EmailField('Email', max_length=300, blank=False, null=False)

    def __str__(self):
        return self.name
