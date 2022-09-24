from django.urls import path

from myblog.views import index, post, contact

urlpatterns = [
    path('', index),
    path('post_detail/', post),
    path('contact/', contact),
]
