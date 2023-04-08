from django import forms
from .models import Post, Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'active')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Category name'}),
        }

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Category.objects.filter(title__iexact=title)
        if qs.exists():
            self.add_error('title', f"The title, '{title}' already exists.")
        return data


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'active')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Category name'}),
        }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'content', 'active')

        widgets = {
            'content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder':'Content', 'rows':'5'}),
            'category': forms.Select(attrs = {'class': 'form-select'}),
        }

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Post.objects.filter(title__iexact=title)
        if qs.exists():
            self.add_error('title', f"The title, '{title}' has already exist.")
        return data


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'content', 'active')

        widgets = {
            'content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder':'Content', 'rows':'5'}),
            'category': forms.Select(attrs = {'class': 'form-select'}),
            }