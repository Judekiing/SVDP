from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

class ReadingPageView(TemplateView):
    template_name = 'daily_reading.html'

class MassPageView(TemplateView):
    template_name = 'mass_times.html'

class OrganisationView(TemplateView):
    template_name = 'society.html'

class ReflectionsView(TemplateView):
    template_name = 'buletn.html'





