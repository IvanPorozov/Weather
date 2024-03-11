from django.db import models


class PlaceForWalk(models.Model):
    img = models.ImageField()
    name = models.TextField(max_length=35)
    description = models.TextField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return self.name


class Categories(models.Model):
    cat = models.TextField(max_length=25)

    def __str__(self):
        return self.cat
