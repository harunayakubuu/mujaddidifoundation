from django.urls import path
from . import views 

app_name = 'contacts'

urlpatterns = [
    path('contact-form/', views.contact_form, name = 'contact_form'),
    path('messages/', views.contact_messages, name = 'contact_messages'),
    path('message/<int:id>/details/', views.message_details, name = 'message_details'),
    path('message/<int:id>/update/', views.message_update, name = 'message_update'),
    path('message/<int:pk>/delete/', views.MessageDeleteView.as_view(), name = 'message_delete'),
]