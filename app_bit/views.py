from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your views here.

def home(request):
  return render(request, "app_bit/home.html")

class AboutView(ListView):
  model = User
  queryset = User.objects.order_by("username")
  template_name = 'app_bit/about.html'
  context_object_name = 'users'

def rules(request):
  return render(request, "app_bit/rules.html")
