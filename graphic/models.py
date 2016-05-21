from __future__ import unicode_literals
from django.db import models

class Arquivo(models.Model):
    arq = models.FileField();
