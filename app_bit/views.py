import os
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views import View
# Create your views here.


def home(request):
    return render(request, "app_bit/home.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                 "url": os.environ.get("DOMAIN_URL")})


class AboutView(ListView):
    model = User
    queryset = User.objects.order_by("username")
    template_name = 'app_bit/about.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"facebook": os.environ.get("FACEBOOK_ID"),
                        "url": os.environ.get("DOMAIN_URL")})
        return context


def rules(request):
    return render(request, "app_bit/rules.html", {"facebook": os.environ.get("FACEBOOK_ID"),
                                                  "url": os.environ.get("DOMAIN_URL")})


def AdView(request):
    line = os.environ.get("AD_TXT")
    return HttpResponse(line)
