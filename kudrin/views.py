from django.shortcuts import render, redirect, get_object_or_404
from .utils import paginator
from .models import News, Store, BookShelf, Review, BuyQuery


def index(request):
    return render(request, 'kudrin/index.html')


def news(request):
    posts = News.objects.all()
    context = {
        'page_obj': paginator(request, posts)
    }
    return render(request, 'kudrin/news.html', context)


def bookshelf(request):
    books = BookShelf.objects.all()
    context = {
        'page_obj': paginator(request, books)
    }
    return render(request, 'kudrin/bookshelf.html', context)


def store(request):
    merchs = Store.objects.all()
    context = {
        'page_obj': paginator(request, merchs)
    }
    return render(request, 'kudrin/store.html', context)


def news_detail(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'kudrin/news_detail.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(BookShelf, pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'kudrin/book_detail.html', context)


def store_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    context = {
        'store': store
    }
    return render(request, 'kudrin/store_detail.html', context)

def book_query(request, book_id):
    return render(request, 'kudrin/query.html')


def book_review(request, book_id):
    reviews = Review.objects.all()
    context = {
        'page_obj': paginator(request, reviews)
    }
    return render(request, 'kudrin/reviews.html', context)

def create_review(request, book_id):
    review = Review.objects.all()
    context = {
        'review': review
    }
    return render(request, 'kudrin/create_review.html', context)
