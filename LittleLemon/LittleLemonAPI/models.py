from django.db import models

# Create your models here.

class Category(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

class MenuItem(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


