from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    fields = ['name', 'country','coordination_x', 'coordination_y', 'image']

admin.site.register(City, CityAdmin)