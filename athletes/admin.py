from django.contrib import admin
from .models import *


@admin.register(Trainer)
class AdminTrainer(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Athlete)
class AdminAthlete(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_place')
