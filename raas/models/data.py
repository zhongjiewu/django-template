from django.db import models
from raas.models import DomainConfig


class RecResults(models.Model):
    """Recommendation results"""
    class Meta:
        app_label = 'raas'

    domain = models.ForeignKey(DomainConfig)
    source = models.IntegerField(default=-1)
    target = models.IntegerField(default=-1)
    score = models.FloatField(default=0)


# a temporary model to save amazon product info
class Product(models.Model):
    class Meta:
        app_label = 'raas'

    domain = models.ForeignKey(DomainConfig)
    title = models.TextField(default="")
    pid = models.IntegerField(default=-1)
    image = models.URLField(max_length=500, default="")
    link = models.URLField(max_length=500, default="")
    product_group = models.CharField(max_length=255, default="")
    brand = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    list_price = models.FloatField(default=0)
    manufacturer = models.CharField(max_length=100, default="")
