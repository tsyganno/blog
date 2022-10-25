from django.shortcuts import render
from django.views import View
from myblog.models import Post
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/home.html', context={'page_obj': page_obj})


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'myblog/post_detail.html', context={'post': post})


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

