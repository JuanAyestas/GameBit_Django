from django.urls import path
from .views import (MemeListView, MemeDetailView, MemeCreateView, 
                    MemeUpdateView, MemeDeleteView, MemeSearchResult)
from . import views

urlpatterns = [
    path('', MemeListView.as_view(), name="gamebit-meme"),
    path("new/", MemeCreateView.as_view(), name="gamebit-meme-create"),
    path("search/", MemeSearchResult.as_view(), name="gamebit-meme-search"),
    path("<int:pk>/", MemeDetailView.as_view(), name="gamebit-meme-full"),
    path("<int:pk>/edit/", MemeUpdateView.as_view(), name="gamebit-meme-edit"),
    path("<int:pk>/delete/", MemeDeleteView.as_view(), name="gamebit-meme-delete"),
]
