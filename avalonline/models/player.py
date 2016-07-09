from django.db import models


class Roles(object):
    WHITE = "white"
    BLACK = "black"
ROLE_CHOICES = [
    (value, value) for attr, value in sorted(Roles.__dict__.items()) if not attr.startswith("_")
]


class Player(models.Model):
    nickname = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    game = models.ForeignKey('Game', related_name="players")
