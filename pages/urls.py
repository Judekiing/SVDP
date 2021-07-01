from django.urls import path
from django.urls import path

from .views import(
     HomePageView, ReadingPageView, 
     MassPageView, BulletinPageView,
    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reading/', ReadingPageView.as_view(), name='reading'),
    path('mass/', MassPageView.as_view(), name='mass_times'),
    path('bulletin/', BulletinPageView.as_view(), name='bulletin'),



]