import django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from twilio.rest import Client


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('phone_number', type=str)

    def handle(self, *args, **options):
        from_ = settings.TWILIO_FROM_NUMBER
        to = options['phone_number']
        version = django.get_version()
        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )
        client.api.account.messages.create(
            to=to,
            from_=from_,
            body=f"Hello, this is a test message from Django {version}!"
        )
        self.stdout.write(f"Sent a text message from {from_} to {to}.")
