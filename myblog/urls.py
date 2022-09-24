from django.urls import path

from myblog.views import index, post

urlpatterns = [
    path('', index),
    path('post_detail/', post),
]
