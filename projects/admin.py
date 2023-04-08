from django.contrib import admin
from .models import Category, Project


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('active', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'category', 'budget', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('project_name',)}

admin.site.register(Project, ProjectAdmin)