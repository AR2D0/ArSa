"""
Admin configuration for DateRequest.
"""
from django.contrib import admin
from .models import DateRequest


@admin.register(DateRequest)
class DateRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'selected_date', 'selected_time',
        'location_name', 'ip_address', 'created_at'
    )
    list_filter = ('selected_date', 'created_at', 'user')
    search_fields = (
        'user__username', 'user__display_name',
        'location_name', 'ip_address'
    )
    readonly_fields = ('created_at', 'ip_address')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'selected_date', 'selected_time')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude', 'location_name')
        }),
        ('Metadata', {
            'fields': ('ip_address', 'created_at')
        }),
    )
