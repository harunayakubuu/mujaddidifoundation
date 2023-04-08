from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.donations, name = 'donations'),
    path('donate/', views.donate, name = 'donate'),
    path('donors/', views.donors, name = 'donors'),
]