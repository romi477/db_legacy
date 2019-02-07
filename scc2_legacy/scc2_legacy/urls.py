from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import redirect_to_home

urlpatterns = [
    path('', redirect_to_home),
    path('admin/', admin.site.urls),
    path('stereolife/', include('cinemas.urls')),
    path('stereolife/auth/', include('authorization.urls')),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



