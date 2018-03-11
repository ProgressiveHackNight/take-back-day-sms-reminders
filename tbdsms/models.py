from django.db import models


class AlertRecipient(models.Model):
    ENGLISH = 'en'
    SPANISH = 'es'

    LANGUAGE_CHOICES = (
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
    )

    phone_number = models.CharField(
        max_length=10,
    )

    zip_code = models.CharField(
        max_length=10,
        blank=True,
    )

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="Location to drop off opioids",
    )

    location_link = models.URLField(
        max_length=500,
        blank=True,
        help_text="Google Maps link to location",
    )
