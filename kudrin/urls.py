from django.urls import path

from . import views

app_name = 'kudrin'

urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('news/', views.news, name='news'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('store/', views.store, name='store'),
    path('info', views.info, name='info'),
    path('news/<int:post_id>', views.news_detail, name='news_detail'),
    path('bookshelf/<int:book_id>', views.book_detail, name='book_detail'),
    path('store/<int:store_id>/query', views.store_query, name='store_query'),
    path('bookshelf/<int:book_id>/query', views.book_query, name='book_query'),
    path('bookshelf/<int:book_id>/reviews', views.book_review, name='book_review'),
    path('bookshelf/<int:book_id>/create_review', views.create_review, name='create_review'),
]
