from django import forms
from .models import FoundationCommittee


class FoundationCommitteeMemberForm(forms.ModelForm):
    class Meta:
        model = CommitteeMemberForm
        fields = ['user', 'designation', 'words', 'display_picture', 'about', 'qualification', 'experience', 'active']