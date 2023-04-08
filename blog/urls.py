from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('posts/', views.posts, name = 'posts'),
    path('post/<str:slug>/', views.post_details, name = 'post_details'),

    path('all/posts/', views.all_posts, name = 'all_posts'),
    path('create/form/', views.post_create, name = 'post_create'),
    path('<int:id>/edit/', views.post_update, name = 'post_update'),
    path('<int:id>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),

    path('categories/', views.categories, name = 'categories'),
    path('category/create/form/', views.category_create, name = 'category_create'),
    path('category/<int:id>/edit/', views.category_edit, name = 'categoy_edit'),
    path('category/<int:id>/delete/', views.CategoryDeleteView.as_view(), name = 'category_delete')
]