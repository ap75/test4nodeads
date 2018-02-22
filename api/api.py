from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from .models import Group, Element


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'

    def dehydrate(self, bundle):
        bundle.data['group_count'] = Group.objects.filter(parent=bundle.obj.id).count()
        bundle.data['elem_count'] = Element.objects.filter(group=bundle.obj.id).count()
        return bundle


class ElementResource(ModelResource):
    group = fields.ForeignKey(GroupResource, 'group', blank=True, null=True)

    class Meta:
        queryset = Element.objects.all()
        resource_name = 'element'
        filtering = {
            'group': ALL_WITH_RELATIONS
        }

    def get_object_list(self, request):
        return super(ElementResource, self).get_object_list(request).filter(checked=True)