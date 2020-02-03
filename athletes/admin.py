from django.contrib import admin
from .models import Trainer, Athlete
from django.utils.safestring import mark_safe
from core.settings import MEDIA_URL


@admin.register(Trainer)
class AdminTrainer(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Athlete)
class AdminAthlete(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_place', 'image')

    def image(self, obj):
        return mark_safe('<image height="25" width="25" src="{}/{}" />'.format(MEDIA_URL, obj.picture))
