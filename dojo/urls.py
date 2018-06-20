from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    #dojo/sum/숫자/숫자 인데 x 와 y는 변수에 속하고 이것을 views.mysum함수의 인자로 넘긴다.
    #어떠한 페턴이 들어오면 함수를 실행 하겠다.
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<a>\d+)/$', views.mysum),

    #dojo/hello/한글이름/나이
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^list4/$', views.excel_download),


    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    # url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^cbv/list4/$', views_cbv.excel_download),
]
