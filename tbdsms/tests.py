import pytest

from .models import Location, AlertRecipient


@pytest.mark.django_db
def test_minimal_alert_recipient_works():
    ar = AlertRecipient(phone_number='1234567890')
    ar.full_clean()
    ar.save()


@pytest.mark.django_db
def test_location_works():
    loc = Location(
        name='Duane Reade FH',
        type='Pharmacy',
        address='71-10 67th Avenue Forest Hills 11375',
        latitude=79.222345,
        longitude=-108.211
    )
    loc.full_clean()
    loc.save()
