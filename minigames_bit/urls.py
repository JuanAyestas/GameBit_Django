from django.urls import path
from . import views

urlpatterns = [
    path('', views.MiniGames, name="gamebit-minigames"),
    path('coin/', views.coin, name="gamebit-coin"),
    path('cup/', views.cup, name="gamebit-cup"),
]
