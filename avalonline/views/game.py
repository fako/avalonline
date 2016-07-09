from django.shortcuts import render_to_response, RequestContext, Http404
from django.views.generic import TemplateView

from avalonline.models.game import Game

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
        game = Game.object.create(qr_code="")
        return render_to_response(self.template_name, {"game": game}, RequestContext(request))