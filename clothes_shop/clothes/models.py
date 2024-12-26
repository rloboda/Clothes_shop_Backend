from django.db import models

class Cloth(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField()
    category = models.TextField(null=True)