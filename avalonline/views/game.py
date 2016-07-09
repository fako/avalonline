import os
from io import StringIO, BytesIO
import qrcode
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext, Http404
from django.views.generic import TemplateView
from django.core.files.uploadedfile import InMemoryUploadedFile

from avalonline.models import Game, Player


class GameView(TemplateView):
    template_name = "game.html"


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

        game = Game.objects.create()
        player = Player.objects.create(game=game, nickname=request.POST.get("nickname"))
        qr_code = qrcode.make(reverse("player", args=(game.id,)))
        game.game_master = player

        #game.qr_code = qr_code.get_image()
        buffer = BytesIO()
        qr_code.save(buffer)
        filename = 'qr-code.{}.png'.format(game.id)

        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.seek(0, os.SEEK_END), None
        )
        game.qr_code.save(filename, filebuffer)
        game.save()
        return render_to_response(self.template_name, {"game": game, "player": player}, RequestContext(request))


def start_game(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise Http404('Game {} does not exist'.format(game_id))
    game.assign_player_roles()
    return render_to_response("start.html", {"game": game}, RequestContext(request))
