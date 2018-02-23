import json

from django.test import TestCase

from .models import Element, Group


class ApiTestCase(TestCase):
    def test_listing_groups(self):
        Group.objects.create(name='Fruit')
        Group.objects.create(name='Vegetables')

        resp = self.client.get('/api/group/')
        self.assertEquals(resp.status_code, 200)

        objects = json.loads(resp.content)['objects']
        self.assertEquals(len(objects), 2)
        self.assertEquals(objects[0]['name'], 'Fruit')
        self.assertEquals(objects[1]['name'], 'Vegetables')


    def test_listing_elements(self):
        group = Group.objects.create(name='Fruit')
        Element.objects.create(group=group, name='Apple', checked=True)
        Element.objects.create(group=group, name='Banana', checked=True)
        Element.objects.create(group=group, name='Cucumber', checked=False)

        resp = self.client.get('/api/element/')
        self.assertEquals(resp.status_code, 200)

        objects = json.loads(resp.content)['objects']
        self.assertEquals(len(objects), 2)
        self.assertEquals(objects[0]['name'], 'Apple')
        self.assertEquals(objects[1]['name'], 'Banana')


    def test_creating_elements(self):
        group = Group.objects.create(name='Fruit')
        post_data = {
            'group': f'/api/group/{group.id}/',
            'name': 'Strawberry',
        }

        resp = self.client.post(
            '/api/element/',
            content_type='application/json',
            data=json.dumps(post_data))
        self.assertEquals(resp.status_code, 201)  # Http Created

        elem = Element.objects.get(name='Strawberry')
        self.assertEquals(elem.group, group)
        self.assertFalse(elem.checked)
