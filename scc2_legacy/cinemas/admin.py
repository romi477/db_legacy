from django.contrib import admin
from .models import Customer, Cinema

admin.site.register(Customer)
admin.site.register(Cinema)

admin.site.site_url = 'http://127.0.0.1:8000/stereolife/'
