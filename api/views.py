#from django.shortcuts import render
from django.views import generic
from django.conf import settings
from .models import Group, Element

class GroupListView(generic.ListView):
    model = Group
    paginate_by = 10
