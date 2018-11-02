from django.urls import path
from . import views

urlpatterns = [
    path('cinemas/', views.hello),
]
