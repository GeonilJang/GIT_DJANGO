
from django.conf.urls import url , include
from django.contrib import admin

from django.conf import settings
from django.shortcuts import redirect

from django.views.generic import RedirectView

# def root(request):
#     return redirect('blog:post_list')



urlpatterns = [
    # url(r'^$', root, name='root'),
    url(r'^$', lambda root: redirect('blog:post_list'), name='root'),
    # url(r'^$', RedirectView.as_view(pattern_name='blog:post_list')),

    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^blog/cbv/new', include('blog.urls')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
