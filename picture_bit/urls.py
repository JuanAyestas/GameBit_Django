from django.urls import path
from .views import ReviewPictureDetail, ReviewPictureDelete


urlpatterns = [
    path("<int:pk>/gallery/", ReviewPictureDetail.as_view(), name="gamebit-gallery"),
    path("<int:review_id>/gallery/<int:pk>/delete/",
         ReviewPictureDelete.as_view(), name="gamebit-pic-delete"),

]
