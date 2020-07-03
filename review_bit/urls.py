from django.urls import path
from .views import (ReviewListView, ReviewDetailView, ReviewCreate, 
                    ReviewUpdateView, ReviewDeleteView, ReviewSearchResult)

urlpatterns = [
    path("", ReviewListView.as_view(), name="gamebit-review"),
    path("new/", ReviewCreate, name="gamebit-create"),
    path("search/", ReviewSearchResult.as_view(), name="gamebit-search"),
    path("<int:pk>/", ReviewDetailView.as_view(), name="gamebit-detail"),
    path("<int:pk>/update/", ReviewUpdateView.as_view(), name="gamebit-update"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="gamebit-delete"),
]
