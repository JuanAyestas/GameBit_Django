import os
from django.shortcuts import render

def acme_content(request):
  return render(request, "app_bit/acme_test.html", 
                {"acme": os.environ.get("LETSENCRYPT_RESPONSE"),
                 "acme_link": os.environ.get("LETSENCRYPT_URL")})
