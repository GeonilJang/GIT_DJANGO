from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products_list, name="products_list" ),
    url(r'^(?P<id>\d+)/$', views.products_detail, name="products_detail"),
    # url(r'^new/$', views.products_new, name='products_new'),
]
# url(r'^$', views.post_list, name='post_list'),
# url(r'^(?P<id>\d+)/$',views.post_detail, name='post_detail'),
