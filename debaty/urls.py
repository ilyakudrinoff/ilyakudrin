from django.urls import path

from . import views

app_name = 'debaty'

urlpatterns = [
    path('debaty', views.debaty, name='debaty'),
    path('results', views.results, name='results'),
    path('createSpeaker', views.createSpeaker, name='createSpeaker'),
]