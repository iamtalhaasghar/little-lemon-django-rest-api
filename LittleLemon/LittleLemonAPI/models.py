from django.db import models

# Create your models here.

class MenuItem(models.Model):

    name = models.TextField()
    price = models.TextField()

    def __str__(self):
        return self.name

    