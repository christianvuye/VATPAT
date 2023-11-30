import pytest
from django.utils import timezone
from dashboard.models import Dealers
from django.db import IntegrityError, OperationalError, DatabaseError

@pytest.fixture
def dealer_instance():
    # Create a Dealer instance
    dealer = Dealers.objects.create(
        D_ID="D001",
        DealerName="Test Dealer",
        DealerVATnumber="VAT12345678",
        DealerEmail="dealer@example.com",
        CreatedDate=timezone.now(),
        ModifiedDate=timezone.now()
    )
    return dealer

@pytest.mark.django_db
def test_dealer_cannot_be_deleted(dealer_instance):
    dealer = dealer_instance

    # Attempt to delete the dealer and expect an error
    with pytest.raises((IntegrityError, OperationalError, DatabaseError)):
        dealer.delete()