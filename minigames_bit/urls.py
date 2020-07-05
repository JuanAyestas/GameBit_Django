from django.urls import path
from .views import MiniGamesView
from . import views

urlpatterns = [
    path('', MiniGamesView.as_view(), name="gamebit-minigames"),
    path('coin/', views.coin, name="gamebit-coin"),
]