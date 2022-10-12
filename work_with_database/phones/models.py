from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')


