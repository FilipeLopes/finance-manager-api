from django.db import models


class Category(models.Model):
    # Aqui colocamos os atributos que esse app vai ter
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
