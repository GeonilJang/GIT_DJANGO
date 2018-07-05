#food/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food_list, name='food_list'),
    url(r'^(?P<id>\d+)/$', views.food_detail, name="food_detail"),
    url(r'^new/$', views.food_new, name="food_new"),
]
