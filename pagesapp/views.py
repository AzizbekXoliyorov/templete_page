from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageview(TemplateView):
    template_name='home.html'

class AboutPageview(TemplateView):
    template_name='about.html'

class FeaturesPageview(TemplateView):
    template_name='features.html'