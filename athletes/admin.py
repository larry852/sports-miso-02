from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Trainer)
class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

admin.site.register(Athlete)
