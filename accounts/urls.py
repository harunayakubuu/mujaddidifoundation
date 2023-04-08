from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('profile/', views.profile, name = 'profile'),
    
    path('users/staff/user/create/form/', views.staff_user_create, name = 'staff-user-create'),
    path('users/user/<str:username>/', views.user_details, name = 'user-details'),
    path('users/user/<int:id>/role/edit/', views.user_role_edit, name = 'user-role-edit'),
    path('user/edit/', views.user_account_edit, name = 'user-account-edit'),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name = 'user-delete'),
]