from django.contrib import admin

# Register your models here.
from .models import Emergency, Car
# admin.site.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'car', 'detail', 'location', 'status')
    # list_filter = ('time', 'category', 'detail')
admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(Car)