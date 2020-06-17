from django.urls import path
from .views import MemeListView, MemeDetailView, MemeCreateView, MemeUpdateView, MemeDeleteView
from . import views

urlpatterns = [
    path('', MemeListView.as_view(), name="gamebit-meme"),
    path("new/", MemeCreateView.as_view(), name="gamebit-meme-create"),
    path("<int:pk>/", MemeDetailView.as_view(), name="gamebit-meme-full"),
    path("<int:pk>/edit/", MemeUpdateView.as_view(), name="gamebit-meme-edit"),
    path("<int:pk>/delete/", MemeDeleteView.as_view(), name="gamebit-meme-delete"),
]
