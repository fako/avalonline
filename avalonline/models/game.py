from django.db import models


class Game(models.Model):
    qr_code = models.ImageField()
    game_master = models.ForeignKey('Player', related_name="+", null=True, blank=True)
