from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from tastypie.api import Api
from .api import GroupResource, ElementResource


api = Api(api_name='api')
api.register(GroupResource())
api.register(ElementResource())

urlpatterns = [
    url(r'^', include(api.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)