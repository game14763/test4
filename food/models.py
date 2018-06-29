from django.db import models

# Create your models here.
class Food(models.Model):
    food = models.CharField(max_length=100)
    sugar = models.CharField(max_length=3)

    def __str__(self):
        return self.food
