import pytest
from django.db.utils import IntegrityError
from django.utils import timezone
from dashboard.models import Dealers

@pytest.mark.django_db
def test_duplicate_d_id_raises_error(test_dealer_instance):
    # Fixture 'test_dealer_instance' from conftest.py is used to create the first dealer instanc
    initial_dealer = test_dealer_instance

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