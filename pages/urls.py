from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-us/', views.about_us, name = 'about_us'),
    path('events/', views.events, name = 'events'),
    path('privacy/', views.privacy, name = 'privacy'),
    path('team/', views.team, name = 'team'),
    path('team-member/<int:id>/', views.team_member, name = 'team_member'),
    path('terms/', views.terms, name = 'terms'),
]