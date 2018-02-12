from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list')  # means that when somehone just enters our site at the base URI, they will be taken to views.post_list
]
