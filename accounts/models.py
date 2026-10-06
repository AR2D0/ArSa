"""
Custom User model for ArSa.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model with display name and role.
    Roles: 'admin' or 'user'
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    display_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Friendly name shown in the UI (e.g. Samina)"
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        help_text="User role determining access level"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def __str__(self):
        return self.display_name or self.username

    @property
    def is_admin_role(self):
        """Check if user has admin role (beyond is_staff/is_superuser)."""
        return self.role == 'admin' or self.is_superuser

    def get_display_name(self):
        return self.display_name or self.username
