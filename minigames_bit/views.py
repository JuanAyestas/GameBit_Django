import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.

class MiniGamesView(ListView):
  model = User
  template_name = 'minigames_bit/mini_games.html'
  context_object_name = 'users'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({"facebook": os.environ.get("FACEBOOK_ID"),
                      "url": os.environ.get("DOMAIN_URL")})
      return context


def coin(request):
  return render(request, "minigames_bit/coin_flip.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                          "url": os.environ.get("DOMAIN_URL")})

