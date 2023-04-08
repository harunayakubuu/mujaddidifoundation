from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()



class Category(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 50, unique = True)
    active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Project(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank = True, null = True)
    project_name = models.CharField(max_length = 200)
    overview = models.TextField()
    budget = models.DecimalField(max_digits = 10, decimal_places = 2)
    progress = models.PositiveIntegerField()
    start_date = models.DateField()
    completion_date = models.DateField()
    picture = models.ImageField(upload_to = 'pictures/projects')

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Complete', 'Complete'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'active')

    slug = models.SlugField(max_length = 50, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
