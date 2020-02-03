from django.contrib import admin
from .models import Participation, Commentary


@admin.register(Participation)
class AdminParticipation(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'youtube_id', 'result')


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ('id', 'comment', 'datetime', 'user')
