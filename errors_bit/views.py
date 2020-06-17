from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    return render(request, 'errors_bit/404.html')


def error_403(request, exception):
    return render(request, 'errors_bit/403.html')


def error_500(request,  exception):
    return render(request, 'errors_bit/500.html')
