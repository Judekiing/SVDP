from django.urls import path


from .views import(
     HomePageView, ReadingPageView, 
     MassPageView, 
     ReflectionsView
    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('refections/', ReflectionsView.as_view(), name='reflections'),
    path('reading/', ReadingPageView.as_view(), name='reading'),
    path('mass/', MassPageView.as_view(), name='mass_times'),




]