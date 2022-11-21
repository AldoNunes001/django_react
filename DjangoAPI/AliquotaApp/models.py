from django.db import models

# Create your models here.


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    produto = models.CharField(max_length=500)
    ncm = models.CharField(max_length=500)
    fecoep = models.DecimalField(max_digits=5, decimal_places=2)
