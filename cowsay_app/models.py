from django.db import models

# Create your models here.


class Cow(models.Model):
    cowsay = models.CharField(max_length=50)

    def __str__(self):
        return self.cowsay
