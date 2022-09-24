from django.urls import path

from myblog.views import index, post, contact, thanks, signup, signin, search

urlpatterns = [
    path('', index),
    path('post_detail/', post),
    path('contact/', contact),
    path('thanks/', thanks),
    path('signup/', signup),
    path('signin/', signin),
    path('search/', search),
]
