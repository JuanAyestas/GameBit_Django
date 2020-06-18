from django.shortcuts import render

# Create your views here.

def error_404(request, exception):
    return render(request, 'errors_bit/404.html', status=404)


def error_403(request, exception):
    return render(request, 'errors_bit/403.html', status=403)


def error_500(request,  exception):
    return render(request, 'errors_bit/500.html', status=500)
