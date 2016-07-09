from django.contrib import admin

from avalonline.models import Game, Player


class GameAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
