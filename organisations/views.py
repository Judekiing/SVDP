from django.db import models 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Organ


class OrgPageView(ListView):
    model = Organ
    template_name = 'society.html'
    context_object_name = 'all_organ_list'


class OrgDetailView(DetailView):
    model = Organ
    template_name = 'org_detail.html'


class OrgCreate(CreateView):
    model = Organ
    template_name = 'org_new.html'
    fields = '__all__'