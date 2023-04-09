from django.contrib import admin
from .models import FoundationCommittee


class FoundationCommitteeAdmin(admin.ModelAdmin):
    list_display =('name', 'gender', 'designation', 'created_date')
    # search_fields = ('user',)
    ordering = ('-name',)
admin.site.register(FoundationCommittee, FoundationCommitteeAdmin)