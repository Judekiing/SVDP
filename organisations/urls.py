from os import name
from django.urls import path
from .views import OrgPageView, OrgCreate, OrgDetailView

urlpatterns = [
    path('organisation/new/', OrgCreate.as_view(), name='org_new'),
    path('orgnisation/<int:pk>/', OrgDetailView.as_view(), name='org_detail'),
    path('', OrgPageView.as_view(), name='org'),
]