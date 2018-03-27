from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Location(models.Model):
    """
    Represents a location to drop off opioids.
    """

    name = models.CharField(
        max_length=200,
    )

    type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Type of location (e.g. pharmacy)"
    )

    address = models.CharField(
        max_length=200,
    )

    latitude = models.FloatField()

    longitude = models.FloatField()


class AlertRecipient(models.Model):
    """
    Represents an individual who wants to be alerted
    about Take Back Day events.
    """

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

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
