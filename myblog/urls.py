from django.urls import path

from myblog.views import index

urlpatterns = [
    path('', index),
]