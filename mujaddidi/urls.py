from django.conf import settings
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace = 'pages')),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('contacts/', include('contacts.urls', namespace = 'contacts')),
    path('donations/', include('donations.urls', namespace = 'donations')),

    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),

    path('projects/', include('projects.urls', namespace = 'projects')),
    
    path('password-change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm',),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
