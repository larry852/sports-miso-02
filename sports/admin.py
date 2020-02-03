from django.contrib import admin
from .models import Modality, Sport
from django.utils.safestring import mark_safe
from core.settings import MEDIA_URL


@admin.register(Modality)
class AdminModality(admin.ModelAdmin):
    list_display = ('id', 'name', 'sport')


@admin.register(Sport)
class AdminSport(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

    def image(self, obj):
        return mark_safe('<image height="25" width="25" src="{}/{}" />'.format(MEDIA_URL, obj.icon))
