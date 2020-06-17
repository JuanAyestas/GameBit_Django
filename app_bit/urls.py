from django.urls import path
from .views import AboutView
from . import views

urlpatterns = [
    path('', views.home, name="gamebit-home"),
    path('about/', AboutView.as_view(), name="gamebit-about"),
    path('rules/', views.rules, name="gamebit-rule"),
]
