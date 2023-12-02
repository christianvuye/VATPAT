import pytest
from django.utils import timezone
from dashboard.models import Dealers

@pytest.fixture(scope='module')
def test_dealer_data():
    """Fixture to provide dealer data dictionary."""
    return {
        "D_ID": "D001",
        "DealerName": "Test Dealer",
        "DealerVATnumber": "VAT12345678",
        "DealerEmail": "dealer@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }

@pytest.fixture(scope='module')
def test_dealer_instance(test_dealer_data):
    """Fixture to create and return a dealer instance."""
    return Dealers.objects.create(**test_dealer_data)