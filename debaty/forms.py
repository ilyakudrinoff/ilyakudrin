from django import forms

from .models import Team, Speaker


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'company',)
        labels = {'name': 'Название команды', 'company': 'Организация',}


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ('lastName', 'name', 'serName', 'team',)
        labels = {'lastName': 'Фамилия', 'name': 'Имя', 'serName': 'Отчество', 'team': 'Команда',}