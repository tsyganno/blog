from django.shortcuts import render


def index(request):
    return render(request, 'myblog/home.html')


def post(request):
    return render(request, 'myblog/post_detail.html')


def contact(request):
    return render(request, 'myblog/contact.html')