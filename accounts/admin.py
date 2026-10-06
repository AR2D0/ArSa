"""
Admin configuration for custom User model.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 'display_name', 'role', 'email',
        'is_staff', 'is_active', 'created_at'
    )
    list_filter = ('role', 'is_staff', 'is_active', 'created_at')
    search_fields = ('username', 'display_name', 'email')
    ordering = ('-created_at',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('ArSa Profile', {
            'fields': ('display_name', 'role', 'created_at'),
        }),
    )
    readonly_fields = ('created_at',)

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('ArSa Profile', {
            'fields': ('display_name', 'role'),
        }),
    )
