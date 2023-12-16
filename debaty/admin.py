from django.contrib import admin
from .models import News, Team, Speaker, ResultsSpeaker, ResultsTeam


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'text',)
    search_fields = ('title','text',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'company',)
    list_filter = ('company',)
    search_fields = ('name','company',)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'name', 'serName', 'team')
    list_filter = ('team',)
    search_fields = ('lastName','name', 'team',)


@admin.register(ResultsSpeaker)
class ResultsSpeakerAdmin(admin.ModelAdmin):
    list_display = ('speaker', 'result',)


@admin.register(ResultsTeam)
class ResultsTeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'result',)
