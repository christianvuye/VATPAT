import pytest
from django.utils import timezone
from dashboard.models import Dealers

@pytest.fixture
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

@pytest.fixture
def test_dealer_instance(test_dealer_data):
    """Fixture to create and return a dealer instance."""
    return Dealers.objects.create(**test_dealer_data)

@pytest.fixture
def test_dealer_data_no_timestamps():
    """Fixture to provide dealer data without timestamps."""
    return {
        "D_ID": "D002",  # Ensure unique D_ID for testing
        "DealerName": "Auto Timestamp Dealer",
        "DealerVATnumber": "VAT87654321",
        "DealerEmail": "auto@example.com"
    }

@pytest.fixture
def test_dealer_instance_no_timestamps(test_dealer_data_no_timestamps):
    """Fixture to create a dealer instance without manually setting timestamps, using the provided dealer data."""
    return Dealers.objects.create(**test_dealer_data_no_timestamps)
