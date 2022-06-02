from django.urls import path
from .views import HomePageview,AboutPageview,FeaturesPageview

urlpatterns=[
    path('features/',FeaturesPageview.as_view(),name='features'),
    path('about/',AboutPageview.as_view(),name='about'),
    path('', HomePageview.as_view(), name='home')
]