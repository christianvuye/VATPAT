import pytest
from django.utils import timezone
from dashboard.models import Dealers

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_dealers():   
    now = timezone.now()  # This will be a timezone-aware datetime object
    
    Dealers.objects.create(
        D_ID='D001',
        DealerName='Test Dealer',
        DealerVATnumber='123456789',
        DealerEmail='test@example.com',
        CreatedDate=now,
        ModifiedDate=now
    )

    all_dealers = Dealers.objects.all()

    # Ensure we can fetch dealers, indicating no basic mismatch
    assert all_dealers.exists(), "Failed to fetch dealers from the database."