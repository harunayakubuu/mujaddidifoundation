from django.contrib import admin
from .models import Event, FoundationCommittee


class FoundationCommitteeAdmin(admin.ModelAdmin):
    list_display =('name', 'gender', 'designation', 'created_date')
    # search_fields = ('user',)
    ordering = ('-name',)
admin.site.register(FoundationCommittee, FoundationCommitteeAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_location', 'event_picture', 'event_date', 'event_start_time', 'event_end_time')
    # search_fields = ('user',)
    ordering = ('-event_date',)
admin.site.register(Event, EventAdmin)