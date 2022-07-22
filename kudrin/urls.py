from django.urls import path

from . import views

app_name = 'kudrin'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('store/', views.store, name='store'),
]
