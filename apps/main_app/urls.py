from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)$', views.show_profile),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_profile),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update_profile),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy_profile),
]
