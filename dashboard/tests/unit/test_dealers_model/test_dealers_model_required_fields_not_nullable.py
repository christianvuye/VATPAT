import pytest
from django.db import transaction
from django.db.utils import IntegrityError
#from django.utils import timezone
from dashboard.models import Dealers

"""@pytest.fixture
def dealer_data():
    return {
        "D_ID": "D001",
        "DealerName": "First Dealer",
        "DealerVATnumber": "VAT12345678",
        "DealerEmail": "firstdealer@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now()
    }"""

@pytest.mark.django_db
def test_dealers_model_required_fields_not_nullable(test_dealer_data):
    for field in test_dealer_data:
        data_with_null_field = test_dealer_data.copy()
        data_with_null_field[field] = None

        with transaction.atomic():  # Wrap the test in an atomic block
            with pytest.raises(IntegrityError) as excinfo:
                Dealers.objects.create(**data_with_null_field).full_clean()

        # Update the assertion if necessary to match the SQL Server error message
        assert "Cannot insert the value NULL" in str(excinfo.value), f"IntegrityError not raised for null {field}"

