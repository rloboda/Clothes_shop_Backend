from django.db import models

class Cloth(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default = 'default.png')