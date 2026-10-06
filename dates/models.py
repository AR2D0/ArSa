"""
DateRequest model for ArSa invitation system.
"""
from django.conf import settings
from django.db import models


class DateRequest(models.Model):
    """
    Stores a date invitation request submitted by a user.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='date_requests'
    )
    selected_date = models.DateField(
        help_text="The chosen date for the invitation"
    )
    selected_time = models.TimeField(
        help_text="The chosen time for the invitation"
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude of the selected location"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude of the selected location"
    )
    location_name = models.CharField(
        max_length=255,
        blank=True,
        default='',
        help_text="Human-readable location name (optional reverse geocode)"
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        help_text="IP address of the user at submission time (admin only)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Date Request'
        verbose_name_plural = 'Date Requests'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} – {self.selected_date} {self.selected_time}"

    @property
    def formatted_datetime(self):
        return f"{self.selected_date.strftime('%B %d, %Y')} at {self.selected_time.strftime('%I:%M %p')}"
