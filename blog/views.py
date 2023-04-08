from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Post, Category
from .forms import PostCreateForm, PostEditForm, CategoryCreateForm, CategoryEditForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy


@login_required
def categories(request):
    categories = Category.objects.order_by('-created_at')
    context = {
        'categories': categories
    }
    return render(request, 'blog/categories.html', context)


@login_required
def category_create(request):
    form = CategoryCreateForm()
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Created.')
            return redirect('blog:categories')
    context = {
        'form': form
    }
    return render(request, 'blog/category-create.html', context)


@login_required
def category_edit(request, id):
    category = Category.objects.get(id = id)
    category_edit_form = CategoryEditForm(instance = category)
    if request.method == 'POST':
        category_edit_form = CategoryEditForm(request.POST, instance = category)
        if category_edit_form.is_valid():
            category_edit_form.save()
            messages.success(request, 'Post updated successfull.')
            return redirect('blog:categories')
    context = {
        'category_edit_form': category_edit_form,
        'categor': category
    }
    return render(request, 'blog/category-edit.html', context)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'blog/category-delete.html'
    success_url = reverse_lazy('blog:categories')


# Public
def posts(request):
    activities = Post.objects.order_by('-created_at').filter(active=True)
    paginator = Paginator(activities, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request, 'blog/posts.html', context)


def post_details(request, slug):
    categories = Category.objects.order_by('title')
    post = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.order_by('-created_at').filter(category=post.category).exclude(id=post.id)[:6]
    context = {
        'post':post,
        'related_posts': related_posts,
        'categories': categories
    }
    return render(request, 'blog/post_details.html', context)


@login_required
def all_posts(request):
    all_posts = Post.objects.order_by('-created_at')
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all_posts.html', context)


@login_required
def post_create(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'Post Created.')
            return redirect('blog:all_posts')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required
def post_update(request, id):
    post = Post.objects.get(id = id)
    update_form = PostUpdateForm(instance = post)
    if request.method == 'POST':
        update_form = PostUpdateForm(request.POST, request.FILES, instance = post)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Post updated successfull.')
            return redirect('blog:all_posts')
    context = {
        'update_form': update_form,
        'post': post
    }
    return render(request, 'blog/post_update.html', context)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:all_posts')