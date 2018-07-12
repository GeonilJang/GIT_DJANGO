#review/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^register/$', views.review_regi, name='review_regi'),
]
