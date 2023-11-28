import pytest
from django.utils import timezone
from dashboard.models import Dealers

@pytest.fixture
def create_dealer():
    now = timezone.now()  # This will be a timezone-aware datetime
    return Dealers.objects.create(
        D_ID='D001',
        DealerName='Test Dealer',
        DealerVATnumber='123456789',
        DealerEmail='test@example.com',
        CreatedDate=now,
        ModifiedDate=now
    )

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_dealers(create_dealer):   
    all_dealers = Dealers.objects.all()

    # Ensure we can fetch dealers, indicating no basic mismatch
    assert all_dealers.exists(), "Failed to fetch dealers from the database."
    assert create_dealer in all_dealers, "Created dealer is not in the database."