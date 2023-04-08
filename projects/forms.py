from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'category', 'project_name',
            'overview', 'budget', 'progress',
            'start_date', 'completion_date',
            'picture', 'status'
        )