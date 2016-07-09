from django.db import models


class Game(models.Model):
    qr_code = models.ImageField()
    game_master = models.ForeignKey('Player', related_name="+", null=True, blank=True)

    def assign_player_roles(self):
        # TODO: take random X players (X is defined per len(players)). Set these players to role "black" set all others to role "white"
        return
