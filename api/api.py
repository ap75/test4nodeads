from tastypie import fields
from tastypie.resources import ModelResource
from .models import Group, Element


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'


class ElementResource(ModelResource):
    group = fields.ForeignKey(GroupResource, 'group', blank=True, null=True)
    class Meta:
        queryset = Element.objects.filter(checked=True)
        resource_name = 'element'