#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    #^시작 $끝
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)$',views.post_detail),


    url(r'^test/(?P<name>[ㄱ-힣]+)/$', views.test),

]
