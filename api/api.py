from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from .models import Group, Element


class GroupResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent', blank=True, null=True)
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        filtering = {
            'parent': ALL_WITH_RELATIONS
        }

    def dehydrate(self, bundle):
        bundle.data['group_count'] = Group.objects.filter(parent=bundle.obj.id).count()
        bundle.data['elem_count'] = Element.objects.filter(group=bundle.obj.id, checked=True).count()
        return bundle
        # или переделать queryset с annotate()?


class ElementResource(ModelResource):
    group = fields.ForeignKey(GroupResource, 'group')
    #icon = fields.FileField(attribute="img")
    created = fields.DateField(readonly=True)
    checked = fields.BooleanField(readonly=True)

    class Meta:
        queryset = Element.objects.all()
        resource_name = 'element'
        filtering = {
            'group': ALL_WITH_RELATIONS
        }
        authorization = Authorization()

    def get_object_list(self, request):
        return super(ElementResource, self).get_object_list(request).filter(checked=True)