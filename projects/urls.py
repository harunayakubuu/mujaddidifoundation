from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.projects_list, name = 'projects_list'),
    path('add/', views.project_add, name = 'project_add'),
    path('<int:id>/', views.project_details, name = 'project_details'),
]