from os import name
from django.urls import path
from .views import AnnouncementPageView, AnnouncementDetailView, AnnouncementCreate

urlpatterns = [
    path('post/new/', AnnouncementCreate.as_view(), name='annou_new'),
    path('post/<int:pk>', AnnouncementDetailView.as_view(), name='annou_detail'),
    path('', AnnouncementPageView.as_view(), name='annou'),
]