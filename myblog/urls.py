from django.urls import path
from .views import MainView

from myblog.views import MainView, PostDetailView, contact, thanks, signup, signin, search

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('contact/', contact),
    path('thanks/', thanks),
    path('signup/', signup),
    path('signin/', signin),
    path('search/', search),
]
