import qrcode
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext, Http404
from django.views.generic import TemplateView

from avalonline.models import Game, Player


class GameView(TemplateView):
    template_name = "start_avalonline.html"

    def get(self, request, game_id, *args, **kwargs):
        game = None
        if game_id:
            try:
                game = Game.objects.get(id=game_id)
            except Game.DoesNotExist:
                raise Http404('Game {} does not exist'.format(game_id))
        return render_to_response(self.template_name, {"game": game}, RequestContext(request))

    def post(self, request, *args, **kwargs):

        # TODO: create QR code and add to game
        qrcode = qrcode.make(reverse("player"))
        game = Game.object.create(qr_code=qrcode)
        player = Player.objects.create(game=game, nickname=request.POST.get("nickname"))
        game.game_master = player
        game.save()
        return render_to_response(self.template_name, {"game": game, "player": player}, RequestContext(request))


def start_game(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise Http404('Game {} does not exist'.format(game_id))
    return render_to_response("start.html", {"game": game}, RequestContext(request))
