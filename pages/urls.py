from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-us/', views.about_us, name = 'about_us'),
]