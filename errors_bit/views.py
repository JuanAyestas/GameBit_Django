from django.shortcuts import render
from django.views.defaults import page_not_found, HttpResponseForbidden, HttpResponseServerError
# Create your views here.

def handler_404(request, exception):
    return page_not_found(request, exception, template_name='errors_bit/404.html', status=404)


def handler_403(request, exception):
    return HttpResponseForbidden(request, exception, template_name='errors_bit/403.html', status=403)

def error_500(request,  exception):
    return HttpResponseServerError(request,  exception, template_name='errors_bit/500.html', status=500)
