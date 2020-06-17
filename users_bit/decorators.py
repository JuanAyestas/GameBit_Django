from django.http import HttpResponse
from django.shortcuts import redirect, render

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return render(request, "errors_bit/403.html")
        return wrapper_function
    return decorator
