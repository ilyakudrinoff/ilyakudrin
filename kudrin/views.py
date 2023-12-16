from django.shortcuts import render, redirect, get_object_or_404
from .utils import paginator
from .models import News, Store, BookShelf, Review, Author
from .forms import ReviewForm, BuyQueryForm


def index(request):
    return render(request, 'kudrin/index.html')


def author(request):
    authors = Author.objects.all()
    context = {
        'page_obj': paginator(request, authors)
    }
    return render(request, 'kudrin/author.html', context)


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


def store_query(request, store_id):
    form = BuyQueryForm(request.POST or None)
    if form.is_valid():
        shirt = form.save(commit=False)
        shirt.shirt = Store.objects.get(pk=store_id)
        shirt.save()
        return redirect('kudrin:store')
    return render(request, 'kudrin/query.html', {'form': form})


def book_query(request, book_id):
    form = BuyQueryForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = BookShelf.objects.get(pk=book_id)
        review.save()
        return redirect('kudrin:book_detail', book_id)
    return render(request, 'kudrin/query.html', {'form': form})


def book_review(request, book_id):
    reviews = Review.objects.filter(book=book_id)
    context = {
        'page_obj': paginator(request, reviews)
    }
    return render(request, 'kudrin/reviews.html', context)


def create_review(request, book_id):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = BookShelf.objects.get(pk=book_id)
        review.save()
        return redirect('kudrin:book_detail', book_id)
    return render(request, 'kudrin/create_review.html', {'form': form})


def info(request):
    return render(request, 'kudrin/info.html')