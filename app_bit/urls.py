from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="gamebit-home"),
    path('about/', views.AboutView.as_view(), name="gamebit-about"),
    path('rules/', views.rules, name="gamebit-rule"),
    path("ads.txt", views.AdView),
]
