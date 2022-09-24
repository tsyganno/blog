from django.urls import path

from myblog.views import index, post, contact, thanks

urlpatterns = [
    path('', index),
    path('post_detail/', post),
    path('contact/', contact),
    path('thanks/', thanks),
]
