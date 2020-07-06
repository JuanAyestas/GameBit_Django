import os
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def MiniGames(request):
    return render(request, "minigames_bit/mini_games.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                             "url": os.environ.get("DOMAIN_URL")})


def coin(request):
    return render(request, "minigames_bit/coin_flip.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                            "url": os.environ.get("DOMAIN_URL")})


def cup(request):
    return render(request, "minigames_bit/cup_shuffle.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                              "url": os.environ.get("DOMAIN_URL")})
