"""avalonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from avalonline.views.game import GameView
from avalonline.views.player import PlayerView

urlpatterns = [
    url(r'^(?P<game_id>\d+)?$', GameView.as_view(), name="game"),
    url(r'^(?P<game_id>\d+)/player/(?P<player_id>)?$', PlayerView.as_view(),name="player"),
    url(r'^(?P<game_id>\d+)/start/$', PlayerView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
]
