from django.shortcuts import render
from django.views import View
from .models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'myblog/home.html', context={
            'posts': posts
        })


def post(request):
    return render(request, 'myblog/post_detail.html')


def contact(request):
    return render(request, 'myblog/contact.html')


def thanks(request):
    return render(request, 'myblog/thanks.html')


def signup(request):
    return render(request, 'myblog/signup.html')


def signin(request):
    return render(request, 'myblog/signin.html')


def search(request):
    return render(request, 'myblog/search.html')

