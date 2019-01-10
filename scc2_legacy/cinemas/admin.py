from django.contrib import admin
from .models import Customer, Cinema


class CustomAdmin(admin.ModelAdmin):
    list_per_page = 25


admin.site.register(Customer)
admin.site.register(Cinema, CustomAdmin)

admin.site.site_url = 'http://127.0.0.1:8000/stereolife/'

