from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SummaryDetailView
from . import views

urlpatterns = [
    path('register/', views.register, name="gamebit-register"),
    path('register/staff/Bj_hubwWcHH9DsnAxQCuGrDLfjEt79dFVwKzQTxMdk4',views.staff_register, name="gamebit-staff"),
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
