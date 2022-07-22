from django.shortcuts import render


def index(request):
    return render(request, 'kudrin/index.html')


def news(request):
    return render(request, 'kudrin/news.html')


def bookshelf(request):
    return render(request, 'kudrin/bookshelf.html')


def store(request):
    return render(request, 'kudrin/store.html')
