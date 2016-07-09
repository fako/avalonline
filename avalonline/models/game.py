from django.db import models


class Game(models.Model):
    qr_code = models.ImageField()
