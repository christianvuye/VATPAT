import pytest
from django.db.utils import IntegrityError
from dashboard.models import Dealers
from django.utils import timezone

@pytest.mark.django_db
def test_dealers_model_unique(test_dealer_instance):
    # Fixture 'create_initial_dealer' is used to create the first dealer instance
    initial_dealer = test_dealer_instance

    # Attempt to create another dealer with the same D_ID as the initial dealer
    with pytest.raises(IntegrityError):
        Dealers.objects.create(
            D_ID=initial_dealer.D_ID,
            DealerName="Second Dealer",
            DealerVATnumber="VAT87654321",
            DealerEmail="seconddealer@example.com",
            CreatedDate=timezone.now(),
            ModifiedDate=timezone.now()
        )