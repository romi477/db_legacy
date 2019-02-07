from django.urls import path
from .views import *



urlpatterns = [
    path('registration/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]