import pytest
from django.utils import timezone
from dashboard.models import Dealers

@pytest.fixture
def test_dealer_data():
    """Fixture to provide dealer data dictionary."""
    return {
        "D_ID": "PT123456",
        "DealerName": "Test Dealer",
        "DealerVATnumber": "253512182",
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
        "D_ID": "PT123456",  # Ensure unique D_ID for testing
        "DealerName": "Auto Timestamp Dealer",
        "DealerVATnumber": "542915340",
        "DealerEmail": "auto@example.com"
    }

@pytest.fixture
def test_dealer_instance_no_timestamps(test_dealer_data_no_timestamps):
    """Fixture to create a dealer instance without manually setting timestamps, using the provided dealer data."""
    return Dealers.objects.create(**test_dealer_data_no_timestamps)

@pytest.fixture
def test_dealer_data_all_null():
    return {
        "D_ID": None,  # Assuming this is a test case and D_ID is not an AutoField
        "DealerName": None,
        "DealerVATnumber": None,
        "DealerEmail": None,
        "CreatedDate": None,
        "ModifiedDate": None,
    }

@pytest.fixture
def test_dealer_data_valid_vat():
    return {
        "D_ID": "PT123456",
        "DealerName": "Valid VAT Dealer",
        "DealerVATnumber": "594901626",  # Valid VAT number
        "DealerEmail": "auto@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }

@pytest.fixture
def test_dealer_data_invalid_vat():
    return {
        "D_ID": "PT123456",
        "DealerName": "Invalid VAT Dealer",
        "DealerVATnumber": "456789123",  # Invalid VAT number
        "DealerEmail": "auto@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }

@pytest.fixture
def test_dealer_data_valid_d_id():
    return {
        "D_ID": "PT123456",
        "DealerName": "Valid VAT Dealer",
        "DealerVATnumber": "594901626",  # Valid VAT number
        "DealerEmail": "auto@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }

@pytest.fixture
def test_dealer_data_invalid_d_id():
    return {
        "D_ID": "00123456",
        "DealerName": "Valid VAT Dealer",
        "DealerVATnumber": "594901626",  # Valid VAT number
        "DealerEmail": "auto@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }

@pytest.fixture
def test_dealer_data_with_credit_note():
    return {
        "D_ID": "PT123456",
        "DealerName": "Valid VAT Dealer",
        "DealerVATnumber": "594901626",
        "DealerEmail": "auto@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
    }