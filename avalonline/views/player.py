from django.shortcuts import render_to_response, RequestContext, Http404
from django.views.generic import TemplateView

from avalonline.models.game import Game
from avalonline.models.player import Player

class PlayerView(TemplateView):
    template_name = "player.html"

    def get(self, request, game_id, player_id, *args, **kwargs):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            raise Http404('Game {} does not exist'.format(game_id))
        player = None
        if player_id:
            try:
                player = Player.objects.get(id=player_id)
            except Player.DoesNotExist:
                raise Http404('Player {} does not exist'.format(player_id))
        return render_to_response(self.template_name, {"game": game, "player": player}, RequestContext(request))

    def post(self, request, game_id, *args, **kwargs):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            raise Http404('Game {} does not exist'.format(game_id))
        player = Player.objects.create(
            game=game,
            nickname=request.POST.get('nickname')
        )
        return render_to_response(self.template_name, {"game": game, "player": player}, RequestContext(request))
