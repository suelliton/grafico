from __future__ import unicode_literals
from django.db import models

class Arquivo(models.Model):
    arq = models.FileField(upload_to = "/home/suelliton/projetos/grafico/graphic/media");

def __unicode__(self):
    return self.user.username   