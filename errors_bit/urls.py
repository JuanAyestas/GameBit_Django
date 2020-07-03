from django.urls import path
from . import views 

handler404 = 'errors_bit.views.handler_404'
handler500 = 'errors_bit.views.handler_500'
handler403 = 'errors_bit.views.handler_403'
