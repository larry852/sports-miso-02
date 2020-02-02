from django.contrib import admin
from .models import Modality, Sport


@admin.register(Modality)
class AdminModality(admin.ModelAdmin):
    list_display = ('id', 'name', 'sport')


@admin.register(Sport)
class AdminSport(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
