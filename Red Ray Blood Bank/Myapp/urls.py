from django.urls import path
# from django.contrib.auth.decorators import login_required
from . import views

urlpatterns=[
    path('',views.home),    
    path('home/',views.home),
    path('login/',views.login,name='login'),
    path('contact/',views.contact),
    path('nurse/',views.nurse,name='nurse'),
    path('shiftIncharge/',views.shiftIncharge,name='shiftIncharge'),
]
