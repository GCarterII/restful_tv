from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^shows/new+$', views.new_show),
    url(r'^shows/create+$', views.create_show),
    url(r'^shows/(?P<s_id>\d)+$', views.show),
    url(r'^shows/(?P<s_id>\d)/edit+$', views.edit_show),
    url(r'^shows/(?P<s_id>\d)/delete+$', views.delete_show),
    url(r'^shows/+$', views.all_shows),
    url(r'^shows/update+$', views.update_show),
    url(r'^', views.index),
]