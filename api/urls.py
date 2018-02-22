from django.conf.urls import include, url
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from tastypie.api import Api
from .api import GroupResource, ElementResource
from . import views


api = Api(api_name='api')
api.register(GroupResource())
api.register(ElementResource())

urlpatterns = [
    url(r'^', include(api.urls)),
    url(r'^$', views.GroupListView.as_view(), name='list'),
    url(r'^page(?P<page>\d+)/$', views.GroupListView.as_view(), name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except:
        pass
