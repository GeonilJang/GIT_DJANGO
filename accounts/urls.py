
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),

]
