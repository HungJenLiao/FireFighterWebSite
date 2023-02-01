from django.contrib import admin

# Register your models here.
from .models import Emergency
# admin.site.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'unit', 'category', 'detail', 'location')
    list_filter = ('time', 'category', 'detail')
admin.site.register(Emergency, EmergencyAdmin)