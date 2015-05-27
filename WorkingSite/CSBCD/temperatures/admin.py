from django.contrib import admin
from .models import Temperature

# This allows the admin to add data to the database
class TemperatureAdmin(admin.ModelAdmin):
    class Meta:
        model = Temperature

admin.site.register(Temperature, TemperatureAdmin)
