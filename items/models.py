from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


class Item(models.Model):
    # Aqui colocamos os atributos que esse app vai ter
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
