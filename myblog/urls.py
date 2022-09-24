from django.urls import path

from myblog.views import index, post, contact, thanks, signup

urlpatterns = [
    path('', index),
    path('post_detail/', post),
    path('contact/', contact),
    path('thanks/', thanks),
    path('signup/', signup),
]
