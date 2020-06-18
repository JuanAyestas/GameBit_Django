from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SummaryDetailView
from . import views

urlpatterns = [
    path('register/', views.register, name="gamebit-register"),
    path('register/staff/df28fa638d23be003d72cc6330d03efb55301522f521437879e2276c8c4837c1a365236998703b1bf6b8c25c7c9a75ad06f549fb9d47da67bfc40dad1d5693079d6ad9c4571617b9964cec83494a4861f2a874dc74c717c53dc9c7522a171ca02d69817e6e8135beca02cc935e68d8a1addbeeb437da0b49d673b0fcd3499f385c311eba9e53bcc85893d344cc01d0936545dc2b7805f59613be80', views.staff_register, name="gamebit-staff"),
    path("login/", auth_views.LoginView.as_view(template_name="users_bit/login.html"), name="gamebit-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users_bit/logout.html"),name="gamebit-logout"),
    path("password-reset/", 
         auth_views.PasswordResetView.as_view(
             template_name="users_bit/password_reset.html"), name="gamebit-reset"),
    
    path("password-reset/success/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="users_bit/password_reset_done.html"), name="password_reset_done"),
    
    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users_bit/password_reset_confirm.html"), name="password_reset_confirm"),
    
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="users_bit/password_reset_complete.html"), name="password_reset_complete"),
    
    path("profile/", views.profile, name="gamebit-profile"),
    path("summary/<int:pk>/", SummaryDetailView.as_view(), name="gamebit-summary")
]
