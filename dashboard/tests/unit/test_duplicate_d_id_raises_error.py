import pytest
from django.db.utils import IntegrityError
from django.utils import timezone
from dashboard.models import Dealers

@pytest.fixture
def create_initial_dealer():
    return Dealers.objects.create(
        D_ID="D001",
        DealerName="First Dealer",
        DealerVATnumber="VAT12345678",
        DealerEmail="firstdealer@example.com",
        CreatedDate=timezone.now(),
        ModifiedDate=timezone.now()
    )

@pytest.mark.django_db
def test_duplicate_d_id_raises_error(create_initial_dealer):
    # Fixture 'create_initial_dealer' is used to create the first dealer instance
    initial_dealer = create_initial_dealer

    # Attempt to create another dealer with the same D_ID as the initial dealer
    with pytest.raises(IntegrityError) as excinfo:
        Dealers.objects.create(
            D_ID=initial_dealer.D_ID,  # Same D_ID as the first dealer
            DealerName="Second Dealer",
            DealerVATnumber="VAT87654321",
            DealerEmail="seconddealer@example.com",
            CreatedDate=timezone.now(),
            ModifiedDate=timezone.now()
        ).full_clean()  # Calling full_clean to explicitly run model validation

    # Assert that the correct error message is raised
    assert "Violation of UNIQUE KEY constraint" in str(excinfo.value), "Unexpected error message for duplicate D_ID"